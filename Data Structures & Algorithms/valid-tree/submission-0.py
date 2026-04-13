class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge case
        if not n:   # no node, still a tree
            return True

        # set up the adjacent list
        adj = {i : [] for i in range(n)}    # {n1: [n2, ], }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visits = set()
        
        def dfs(curN, prev):                # recursively
            # edge case
            if curN in visits:
                return False
            
            visits.add(curN)
            for adjN in adj[curN]:
                if adjN == prev:    # preventing false True
                    continue
                if not dfs(adjN, curN):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visits)
        
        