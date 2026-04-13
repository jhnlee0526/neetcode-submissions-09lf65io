class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS recursively + hashset for visits + hashmap for the adjacent list
        #   Time : O(n + e), where n = number of nodes, e = number of edges
        #   Space: O(n + e) for the adjacency list + O(n) for the visited set

        # 1. Visited set to track which nodes we've already explored
        visited = set()

        # 2. Prepare to build the adjacency list
        #    adj[node] will hold a list of all neighbors of `node`
        adj = {i: [] for i in range(n)}

        # 3. Populate the adjacency list from the edge list
        #    Since the graph is undirected, we add each edge in both directions
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 4. Define the recursive DFS helper
        def dfs(node):
            """
            Mark `node` and all nodes reachable from it as visited.
            This explores one entire connected component.
            """
            for neighbor in adj[node]:
                # If we haven't visited this neighbor yet, recurse into it
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        # 5. Main loop: for each node, if it's unvisited, it's the start of a new component
        count = 0
        for i in range(n):
            if i not in visited:
                # New component found
                visited.add(i)  # mark the root of this component
                dfs(i)          # flood-fill via DFS to mark the rest
                count += 1      # increment component count

        return count
        