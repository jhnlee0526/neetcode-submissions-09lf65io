class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS iteratively w/ queue + hashset for visits
        #   Time  : O(n + e), where n = number of nodes, e = number of edges
        #   Space : O(n) for visited set and queue

        counts = 0
        visits = set()  # {node, ..}
        adjList = {node: [] for node in range(n)}   # {node : [adjNode, ], ...}
        for n1, n2 in edges:    ##
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        def bfs(curNode):
            q = deque([curNode])  ## fresh queue per component
            visits.add(curNode)
            
            while q:
                qNode = q.popleft()
                for adjNode in adjList[qNode]:
                    if adjNode not in visits:
                        q.append(adjNode)
                        visits.add(adjNode)
        
        for node in range(n):
            if node not in visits:
                counts += 1
                bfs(node)
                
        return counts


        ######################
        # DFS recursively + hashset for visits
        #   Time : O(n + e), where n = number of nodes, e = number of edges
        #   Space : O(n) for visited set and recursion stack

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