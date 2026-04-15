class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Graph: BFS iteratively w/ queue + hashset for visits
        #   time : O(n + e); n = node, e = edge; visits each node only once
        #   space: O(n); hashset for visits
        '''
        VALID TREE must be:
        1. Acyclic (BFS returns TRUE)
        2. Fully connected (All nodes visited)
        '''

        visits = set()  # {node, ..}

        adjMap = {node: [] for node in range(n)}    # {node : [adjNode, ..], ..}
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        
        def bfs(curN, preN):
            q = deque([(curN, preN),])  # [(curNode, preNode), ..]
            while q:
                qCurN, qPreN = q.popleft()
                if qCurN in visits:
                    return False
                
                visits.add(qCurN)

                for adjN in adjMap[qCurN]:
                    if adjN == qPreN:    # SKIP the adge we just came from
                        continue
                    q.append((adjN, qCurN))
                
            return True

        return bfs(0, -1) and n == len(visits)


        # ------------------
        # Graph: DFS recursively + hashset for visits
        #   time : O(n + e); n = node, e = edge; visits each node only once
        #   space: O(n); recursive stacks & hashset for visits

        '''
        VALID TREE must be:
        1. Acyclic (DFS returns TRUE)
        2. Fully connected (All nodes visited)
        '''

        visits = set()  # {node, ..}

        adjList = {node : [] for node in range(n)}   # {node : [adjNode, ..], ..}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(curN, preN):
            # base case
            if curN in visits:
                return False
            
            visits.add(curN)

            for adjN in adjList[curN]:
                if adjN == preN: # SKIP the adge we just came from
                    continue
                if not dfs(adjN, curN):  # curN -> adjN
                    return False
            
            return True


        return dfs(0, -1) and n == len(visits)