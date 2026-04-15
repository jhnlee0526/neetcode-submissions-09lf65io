class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Graph: DFS recursively + hashset for visits
        #   time : O(n + e); n = node, e = edge; visits each node only once
        #   space: O(n + e); recursive stacks & hashset for visits

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