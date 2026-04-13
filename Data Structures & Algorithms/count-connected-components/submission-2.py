class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS recursively + hashset for visits + hashmap for the adj list
        #   Time : O(n + e), where n = number of nodes, e = number of edges
        #   Space: O(n + e) for the adjacency list + O(n) for the visited set

        cnt = 0
        visits = set()                          # {node, ...}
        adjList = {i : [] for i in range(n)}    # {curN : [adjN, ...], ...}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(node):
            if node in visits:  # base case
                return
            
            visits.add(node)
            for adjN in adjList[node]:
                dfs(adjN)
    
        for curN in range(n):
            if curN not in visits:  ##
                dfs(curN)
                cnt += 1
        
        return cnt
