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

        # edge case: the number of edges must be n - 1
        if len(edges) != n - 1:
            return False

        visits = set()  # {node, ..}
        # {node: adjList, node : [adj1, adj2, ..], ..}
        nodeMap = {node : [] for node in range(n)}
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        def bfs(cur, pre):
            q = deque([(cur, pre)]) # [(cur, pre), ..]
            while q:
                qCur, qPre = q.popleft()
                
                if qCur in visits: # detect cycling
                    return False
                
                visits.add(qCur)

                for adj in nodeMap[qCur]:
                    if adj == qPre:
                        continue    # skip
                    q.append((adj, qCur))
            return True

        return bfs(0, -1) and n == len(visits)
