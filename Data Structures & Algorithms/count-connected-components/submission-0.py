class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS recursively + array for visits
        #   Time : O(n + e), where n = number of nodes, e = number of edges
        #   Space: O(n + e) for the adjacency list + O(n) for the visited array

        # 1. Prepare to build the adjacency list
        #    adj[node] will hold a list of all neighbors of `node`
        adj = {i: [] for i in range(n)}  

        # 2. Visited array to mark which nodes we've already explored
        visits = [False] * n

        # 3. Populate the adjacency list from the edge list
        #    Since the graph is undirected, we add each edge in both directions
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # 4. Define the recursive DFS helper
        def dfs(curN):
            """
            Mark `curN` and all nodes reachable from it as visited.
            This explores one entire connected component.
            """
            for nei in adj[curN]:
                # If we haven't visited this neighbor yet, recurse into it
                if not visits[nei]:
                    visits[nei] = True
                    dfs(nei)

        # 5. Main loop: for each node, if it's unvisited, it's the start of a new component
        res = 0
        for node in range(n):
            if not visits[node]:
                # New component found
                visits[node] = True  # mark the root of this component
                dfs(node)            # flood-fill via DFS to mark the rest
                res += 1             # increment component count

        return res
        