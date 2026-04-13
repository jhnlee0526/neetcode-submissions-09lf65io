class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS iteratively w/ queue + hashset for visits
        #   Time  : O(n + e), where n = number of nodes, e = number of edges
        #   Space : O(n) for visited set and queue

        ## edge case: A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        visits = set()
        adjList = {node : [] for node in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def bfs(curNode, prevNode):
            q = deque([(curNode, prevNode)])    # [(curN, prevN), ..]
            while q:
                qCurNode, qPrevNode = q.popleft()
                
                if qCurNode in visits:  # check cycling
                    return False
                visits.add(qCurNode)    ## add to visits after cylcing check

                for adjNode in adjList[qCurNode]:
                    if adjNode == qPrevNode:
                        continue
                    if adjNode not in visits:
                        q.append((adjNode, qCurNode))
                        # visits.add(adjNode)   # TOO SOON. NO NO
            return True

        return bfs(0, -1) and n == len(visits)
        '''
        A VALID TREE must be:
            1. Fully connected (all nodes visited)
            2. Acyclic (BFS returns True)
        '''
        

        ##############################  
        # DFS recursively + hashset for visits
        #   Time  : O(n + e), where n = number of nodes, e = number of edges
        #   Space : O(n) for visited set and recursion stack

        visits = set()  # {node, ..}
        adjList = {node : [] for node in range(n)}  # {node: [adjNode, ..], ..}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        def dfs(curNode, prevNode):
            # base case
            if curNode in visits:   # check cycling
                return False
            
            visits.add(curNode)
            for adjNode in adjList[curNode]:
                if adjNode == prevNode:
                    continue
                if not dfs(adjNode, curNode):
                    return False
            
            return True

        return dfs(0, -1) and n == len(visits)
        '''
        A VALID TREE must be:
            1. Fully connected (all nodes visited)
            2. Acyclic (DFS returns True)
        '''


        