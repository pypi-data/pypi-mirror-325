#%%
import networkx as nx
import itertools

#%%
class CausalQuery:

    def __init__(self, graph):
        if not isinstance(graph, nx.DiGraph):
            raise TypeError("Input graph must be a networkx.DiGraph.")
        self.graph = graph.copy()

    # ----------------------------------------
    #  graph utilities
    # ----------------------------------------
    def ancestors_of_set(self, G, nodes):
        """
        Return the set of all ancestors of 'nodes' in graph G, including each node itself.
        """
        result = set()
        for n in nodes:
            result.update(nx.ancestors(G, n))
            result.add(n)
        return result

    def moralize(self, G):
        """
        Moralize directed graph G by:
          - making it undirected,
          - 'marrying' parents of each node.
        """
        M = nx.Graph()
        M.add_nodes_from(G.nodes())
        # Add undirected edges for every directed edge
        for u, v in G.edges():
            M.add_edge(u, v)
        # Marry the parents of each node
        for node in G.nodes():
            parents = list(G.predecessors(node))
            for i in range(len(parents)):
                for j in range(i + 1, len(parents)):
                    M.add_edge(parents[i], parents[j])
        return M

    def _dsep_moral_test(self, X, Y, Z, moralG):
        """
        Remove Z from an already moralized graph 'moralG'
        and check if X and Y are disconnected.
        """
        test_graph = moralG.copy()
        test_graph.remove_nodes_from(Z)
        return not nx.has_path(test_graph, X, Y)

    # ----------------------------------------
    #  build Effective and Ancestral subgraphs
    # ----------------------------------------
    def _build_effective_graph(self, X, Y, effect):
        """
        For 'total' effect, remove all edges out of X.
        For 'direct' effect, remove only X->Y.
        """
        G_eff = self.graph.copy()
        if effect == "total":
            G_eff.remove_edges_from(list(G_eff.out_edges(X)))
        elif effect == "direct":
            if G_eff.has_edge(X, Y):
                G_eff.remove_edge(X, Y)
        else:
            raise ValueError("Effect must be 'total' or 'direct'.")
        return G_eff

    def _ancestral_subgraph_of_XY(self, X, Y):
        """
        Return the subgraph induced by all nodes that are ancestors of X or Y
        in the original DAG (including X, Y themselves).
        This ensures we keep any path or collider leading into X or Y.
        """
        anXY = self.ancestors_of_set(self.graph, [X, Y])
        return self.graph.subgraph(anXY).copy()

    # ----------------------------------------
    #  build Candidate Set to adjust on
    # ----------------------------------------
    def _build_candidate_adjusters(self, X, Y, effect):
        """
        For 'total': exclude X and all descendants of X (original DAG).
        For 'direct': exclude X, but allow X's descendants.
        Usually also exclude Y from adjusting.
        """
        candidates = set(self.graph.nodes())
        candidates.discard(X)
        if effect == "total":
            desc_X = nx.descendants(self.graph, X)
            candidates -= desc_X
        candidates.discard(Y)
        return candidates

    # ----------------------------------------
    #  find minimal sets by inclusion
    # ----------------------------------------
    def find_adjustment_sets(self, X, Y, effect="total"):
        """
        Return all sets Z that satisfy the back-door criterion for X->Y
        and are *minimal by set inclusion* (i.e., if you remove any variable from Z,
        it no longer blocks the path).
        """
        if X not in self.graph or Y not in self.graph:
            raise ValueError(f"Nodes {X} or {Y} not in the graph.")

        # 1) Build effective graph
        G_eff = self._build_effective_graph(X, Y, effect)

        # 2) Identify all nodes that might appear on a path => ancestors of X or Y
        an_sub = self._ancestral_subgraph_of_XY(X, Y)
        relevant_nodes = set(an_sub.nodes())

        # 3) Induce subgraph in G_eff on those relevant nodes
        sub_eff = G_eff.subgraph(relevant_nodes).copy()

        # 4) Moralize once
        moral_sub_eff = self.moralize(sub_eff)

        # 5) Build candidate set for adjusting (then intersect with relevant_nodes)
        candidates = self._build_candidate_adjusters(X, Y, effect) & relevant_nodes
        candidates = sorted(candidates)

        # Do a DFS/backtracking over 'candidates' to find all minimal sets
        # that d-separate X,Y. Store them in 'minimal_sets'.
        minimal_sets = []

        # For fast pruning, define a helper:
        #    if there's an already-found minimal set S0 that is a subset of S,
        #    then S can't be minimal (since removing S \ S0 would yield S0).
        # So we skip exploring expansions of S.
        def is_superset_of_any_already_found(S):
            # Check if any known minimal set is strictly contained in S
            # (meaning S >= that set in sense of S0 ⊂ S).
            for ms in minimal_sets:
                if ms.issubset(S):
                    return True
            return False

        # The backtracking approach:
        def backtrack(idx, current_set):
            # If current_set already blocks X->Y, record it, prune any superset
            if self._dsep_moral_test(X, Y, current_set, moral_sub_eff):
                # Check minimality: remove any variable and see if it still blocks
                # If removing any var from current_set still blocks => not minimal
                # Do a check
                is_minimal = True
                for var in list(current_set):
                    smaller = current_set - {var}
                    if self._dsep_moral_test(X, Y, smaller, moral_sub_eff):
                        is_minimal = False
                        break
                if is_minimal:
                    # Now also check if it's a superset of any smaller minimal set
                    # (this can happen in more complex graphs).
                    if not is_superset_of_any_already_found(current_set):
                        minimal_sets.append(frozenset(current_set))
                return  # prune supersets of current_set

            # If not blocking yet, or it's not minimal, keep trying to add more candidates
            # but only if we still have candidates left
            for next_idx in range(idx, len(candidates)):
                candidate_node = candidates[next_idx]
                # If including candidate_node makes current_set a superset of a known set => skip
                # (do an early check only if it fully contains a known minimal set.)
                new_set = current_set | {candidate_node}
                if not is_superset_of_any_already_found(new_set):
                    backtrack(next_idx+1, new_set)

        # Initiate DFS with empty set
        backtrack(0, frozenset())

        # Convert from frozenset to normal set, and sort them in a stable way
        # for consistent output
        final_sets = []
        for s in minimal_sets:
            final_sets.append(set(s))
        # Sort by the number of variables then lexicographically
        final_sets.sort(key=lambda ss: (len(ss), sorted(ss)))

        return final_sets

    # ----------------------------------------
    #  Causal Query
    # ----------------------------------------
    def causal_query(self, causal_question=None, effect="total"):
        """
        If causal_question=(X,Y), compute minimal sets for X->Y.
        Otherwise, for each X->Y, gather minimal sets.
        """
        if causal_question is not None:
            X, Y = causal_question
            if X not in self.graph or Y not in self.graph:
                return f"Error: {X} or {Y} not in the graph."

            sets_ = self.find_adjustment_sets(X, Y, effect=effect)
            msg = f"Causal Effect Identification (effect = {effect}):\n"
            msg += f"  Exposure: {X}\n  Outcome: {Y}\n"
            if sets_:
                msg += "  Minimal sufficient adjustment sets (by set inclusion):\n"
                for i, s in enumerate(sets_, start=1):
                    msg += f"    Option {i}: {sorted(s) if s else '∅ (empty)'}\n"
            else:
                msg += "  No valid adjustment set found.\n"
            return msg
        else:
            # Enumerate all pairs X->Y where Y is a descendant of X
            results = {}
            for X_node in self.graph.nodes():
                for Y_node in nx.descendants(self.graph, X_node):
                    sets_ = self.find_adjustment_sets(X_node, Y_node, effect=effect)
                    if sets_:
                        results[(X_node, Y_node)] = sets_
            return results

    def testable_implications(self):
        """
        Enumerate testable implications:
        For every pair (A,B) that are not adjacent in the original DAG,
        find all minimal sets S (by set inclusion) such that A and B
        are d-separated given S in the original DAG.
        Return a list of strings like "A ⊥ B | X1,X2,..."

        Implementation steps:
        1) For each non-adjacent pair (A,B):
            - Build the ancestral subgraph of {A,B}.
            - Moralize it.
            - Let 'candidates' be all nodes except A,B in that subgraph.
            - Do a DFS/backtracking to find all minimal sets that d-separate A,B.
        2) Collect them in a list of strings sorted by (A,B, set).
        """
        # Store the final results (strings)
        all_implications = []

        # Sort nodes for stable iteration order
        nodes_sorted = sorted(self.graph.nodes())

        # Helper to build the moral subgraph once
        def build_moral_subgraph_of_AB(A, B):
            # Induce subgraph on all ancestors of {A,B} in the *original* DAG
            anAB = self.ancestors_of_set(self.graph, [A, B])
            sub_ab = self.graph.subgraph(anAB).copy()
            # Moralize it
            M = self.moralize(sub_ab)
            return M, anAB

        # The d-sep check in moral subgraph
        def dsep_check(A, B, Z, moralG):
            test_g = moralG.copy()
            test_g.remove_nodes_from(Z)
            return not nx.has_path(test_g, A, B)

        # For pruning: if it already found a smaller set S0 that is contained in S,
        # no need to explore S further. (It can't be minimal.)
        def is_superset_of_any(MINIMAL_SETS, S):
            for ms in MINIMAL_SETS:
                if ms.issubset(S):
                    return True
            return False

        # For each pair (A,B) that is NOT adjacent
        for i in range(len(nodes_sorted)):
            for j in range(i+1, len(nodes_sorted)):
                A = nodes_sorted[i]
                B = nodes_sorted[j]

                # Check adjacency in the *original* DAG
                if self.graph.has_edge(A, B) or self.graph.has_edge(B, A):
                    continue  # adjacent => not testable

                # Build moral subgraph of ancestors(A,B)
                moral_ab, anAB = build_moral_subgraph_of_AB(A, B)

                # Candidates: everything in anAB except A,B themselves
                candidates = sorted(set(anAB) - {A, B})

                # Store minimal sets that separate (A,B)
                MINIMAL_SETS = []

                def backtrack(idx, current_set):
                    # Check if current_set d-separates A,B
                    if dsep_check(A, B, current_set, moral_ab):
                        # Check if it's minimal: removing any element unblocks the path
                        is_minimal = True
                        for var in current_set:
                            smaller = current_set - {var}
                            if dsep_check(A, B, smaller, moral_ab):
                                is_minimal = False
                                break
                        if is_minimal:
                            # Also check if current_set is a superset of an already-known set
                            if not is_superset_of_any(MINIMAL_SETS, current_set):
                                MINIMAL_SETS.append(frozenset(current_set))
                        return  # no need to add more variables; bigger sets won't be minimal

                    # Not d-separated yet -> try adding more candidates
                    for next_i in range(idx, len(candidates)):
                        cand_node = candidates[next_i]
                        new_set = current_set | {cand_node}
                        # If new_set is superset of an already-known minimal set => skip
                        if not is_superset_of_any(MINIMAL_SETS, new_set):
                            backtrack(next_i + 1, new_set)

                # Start DFS with empty set
                backtrack(0, frozenset())

                # Build textual output
                # Sort minimal sets by size, then lexicographically
                MINIMAL_SETS = sorted(MINIMAL_SETS, key=lambda s: (len(s), sorted(s)))
                if MINIMAL_SETS:
                    for s in MINIMAL_SETS:
                        if s:
                            cond_list = sorted(s)
                            cond_str = ", ".join(cond_list)
                            all_implications.append(f"{A} ⊥ {B} | {cond_str}")
                        else:
                            all_implications.append(f"{A} ⊥ {B}")  # empty set

        # Sort final output for consistent ordering (e.g. lexicographically)
        all_implications.sort()
        return all_implications

