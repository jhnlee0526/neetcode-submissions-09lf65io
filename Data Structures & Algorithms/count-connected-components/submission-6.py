class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # bfs iteratively with queue + hashmap for visits
        #   Time  : O(n + e), where n = number of nodes, e = number of edges
        #   Space : O(n) for visited set and queue
        
        cnt = 0
        visits = set()  # {node, ..}
        # {node : adj list, node : [adj1, adj2, ..], ..}
        nodeMap = {node : [] for node in range(n)}
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        def bfs(node):
            q = deque([node])
            while q:
                qNode = q.popleft()
                visits.add(qNode)

                for adj in nodeMap[qNode]:
                    if adj not in visits:
                        q.append(adj)

        for node in range(n):
            if node not in visits:
                bfs(node)
                cnt += 1
        return cnt