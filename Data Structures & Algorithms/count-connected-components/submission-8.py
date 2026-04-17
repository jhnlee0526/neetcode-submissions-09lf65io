class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Graph: BFS iteratively with queue + hashset for visits
        #   Time : O(n + e); n = # of nodes, e = # of edges
        #   Space: O(n); queue & hashset for visits 
        
        count = 0
        nodeMap = {node : [] for node in range(n)}    # {node : [adjN, ..], ..}
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        visits = set()  # {node, ..}

        def bfs(node):
            q = deque([node])   # [node, ..]
            while q:
                qNode = q.popleft()
                
                visits.add(qNode)
                for adjN in nodeMap[qNode]:
                    if adjN not in visits:
                        q.append(adjN)


        for node in range(n):
            if node not in visits:
                count += 1
                bfs(node)

        return count

        
        #--------------------------------
        # Graph: DFS recursively + hashset for visits
        #   Time : O(n + e); where n = # of nodes, e = # of edges
        #   Space: O(n); recursive stacks & hashset for visits

        count = 0
        nodeMap = {node : [] for node in range(n)}    # {node: [adjN, ..], ..}
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
