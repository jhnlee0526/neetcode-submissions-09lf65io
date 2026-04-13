class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS recursively + hashset for visits + hasmap for the adjacent nodes
        #   Time : O(N + E)
        #       - N = number of nodes
        #       - E = number of edges
        #       - Each node & edge is visited once
        #   Space: O(N + E)
        #       - Adjacency list + visited set + recursion stack

        # edge case: no node -> still a tree
        if not n:
            return True
        
        visits = set()                          # {node, ...}
        # set up the adjList
        adjList = {i : [] for i in range(n)}    # {node: [adj, ...], ...} 
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        def dfs(curNode, prevNode):
            # base case: already visited. cycling detected!
            if curNode in visits:
                return False
            
            visits.add(curNode)

            # DFS all the adj nodes of this node
            for adjNode in adjList[curNode]:
                # preventing falsy True (SKIP if going back to the prev node)
                if adjNode == prevNode:
                    continue
                if not dfs(adjNode, curNode):
                    return False

            return True
        
        
        return dfs(0, -1) and n == len(visits)  # default prev is -1
        # A VALID TREE must be:
        #   1. Fully connected (all nodes visited)
        #   2. Acyclic (DFS returns True)
