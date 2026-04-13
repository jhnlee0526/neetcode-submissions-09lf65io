class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS recursively + hashset for visits + hashmap for the adjacent list
        #   time : O(n + e), n = node, e = edge, visits each node only once
        #   space: O(n + e)

        visits = set()                          # {node, ...}

        adjList = {i : [] for i in range(n)}    # {curN : [adjN, ...], ...} 
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(curN, prevN):       # prevN for preventing going back to the previous node
            if curN in visits:      # base case
                return False
            
            visits.add(curN)

            for adjN in adjList[curN]:
                if adjN == prevN:   # skip!
                    continue
                if not dfs(adjN, curN):
                    return False
                    
            return True
        
        return dfs(0, -1) and n == len(visits)  # Default prevN is -1
        '''
        A VALID TREE must be:
            1. Fully connected (all nodes visited)
            2. Acyclic (DFS returns True)
        '''


        


        