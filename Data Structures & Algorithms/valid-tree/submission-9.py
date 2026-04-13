class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # bfs iteratively with queue + hashset for visits
        #   Time  : O(n + e), where n = number of nodes, e = number of edges
        #   Space : O(n) for visited set and queue
        '''
            A VALID TREE must be:
                1. Fully connected (all nodes visited)
                2. Acyclic (BFS returns True)
        '''

        # edge case : a valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        visits = set()  # {node, ..}
        # {node : neighbors, node : [adj1, adj2, ..], ..}
        adjList = {node : [] for node in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        def bfs(curN, preN):
            q = deque([(curN, preN)])   # [(curN, preN), ..]
            while q:
                qCurN, qPreN = q.popleft()
                
                if qCurN in visits: # checking cycling
                    return False

                visits.add(qCurN)

                for adjN in adjList[qCurN]:
                    if adjN == qPreN:
                        continue    # skip
                    q.append((adjN, qCurN))

            return True
            
        return bfs(0, -1) and n == len(visits)
        
        
