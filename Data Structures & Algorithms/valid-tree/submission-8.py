class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS iteratively w/ queue + hashset for visits
        #   Time : O(n + e)
        #   Space: O(n)

        # edge case : A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
        
        visits = set()  # {(r, c), ..}
        adjList = {node : [] for node in range(n)}    # {node : [adjNode, ..], ..}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def bfs(curNode, prevNode):
            q = deque([(curNode, prevNode)])    # [(curNode, prevNode), ..]
            
            while q: 
                qCur, qPrev = q.popleft()

                if qCur in visits:
                    return False
                visits.add(qCur)
                
                for adjNode in adjList[qCur]:
                    if adjNode == qPrev:
                        continue
                    q.append((adjNode, qCur))
                
            return True
        
        return bfs(0, -1) and n == len(visits)


        ########################
        # DFS recursively + hashset for visits
        #   Time : O(n + e)
        #   Space: O(n)
        '''
        A VALID TREE must be:
            1. Acyclic (DFS returns True)
            2. Fully connected (all nodes visited)
        '''
        visits = set()  # {node, ..}
        adjList = {node : [] for node in range(n)}    # {node: [adjNode, ..], ..}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(curNode, preNode):
            '''
            We use preNode to avoid falsely detecting cycles in undirected graphs.
            Without it, revisiting the parent node would look like a cycle.
            '''
            # base case
            if curNode in visits:
                return False
            
            visits.add(curNode)
            for adjNode in adjList[curNode]:
                if adjNode == preNode:  # skip the edge we just came from
                    continue
                if not dfs(adjNode, curNode):
                    return False
            
            return True

        return dfs(0, -1) and n == len(visits)
        