class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS recursively + hashset for visits
        #   Time : O(n + e), where n = number of nodes, e = number of edges
        #   Space: O(n + e) for the adjacency list + O(n) for the visited set

        counts = 0
        visits = set()  # {node, ..}
        adjList = {node : [] for node in range(n)}    ## {node : [adjNode, ..]}
        
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(curNode):
            # base case
            if curNode in visits:
                return

            visits.add(curNode)
            
            for adjNode in adjList[curNode]:
                dfs(adjNode)
            
        for node in range(n):
            if node not in visits:
                counts += 1
                dfs(node)
        
        return counts