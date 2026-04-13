"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs recursively 
        #   time : O(n), # of nodes
        #   space: O(n)

        cloneMap = {}   # {og node : cloned node, ..}

        def dfs(node):
            if not node:            # base case 1:
                return None
            if node in cloneMap:    # base case 2: 
                return cloneMap[node]
            
            # clone the current node
            cloneMap[node] = Node(node.val)
            # clone the adjacent nodes by dfs the each adjnode recursively
            for adjNode in node.neighbors:
                cloneMap[node].neighbors.append( dfs(adjNode) )
            
            return cloneMap[node]

        return dfs(node)
            
