class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Graph: DFS recursively + hashset for visits
        #   Time : O(n + e); where n = # of nodes, e = # of edges
        #   Space: O(n); recursive stacks & hashset for visits

        count = 0
        nodeMap = {node : [] for node in range(n)}    # {node: [adj1, ..], ..}
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        visits = set()  # {node, ..}

        def dfs(node):
            # base case
            if node in visits:
                return
            
            visits.add(node)

            for adjN in nodeMap[node]:
                dfs(adjN)
            
        
        for node in range(n):
            if node not in visits:
                count += 1
                dfs(node)
            
        return count
