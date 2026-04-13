class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS recursively + hashset for visits
        #   Time  : O(n + e), where n = number of nodes, e = number of edges
        #   Space : O(n) for visited set and recursion stack

        visits = set()  # {node, ..}
        adjList = {node : [] for node in range(n)}  # {node: [adjNode, ..], ..}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        def dfs(curNode, prevNode):
            if curNode in visits:
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


        