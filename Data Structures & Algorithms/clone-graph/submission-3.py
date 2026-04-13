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
        if not node:
            return None

        ogToCopy = {}   # {ogNode : copyNode, }

        def dfs(node):  # recursively
            # base case
            if node in ogToCopy:        # if already exist, return it
                return ogToCopy[node]
            
            copyNode = Node(node.val)   # create a copy node
            ogToCopy[node] = copyNode   # add the copy node to the map

            for nei in node.neighbors:  # copy neighbors
                ogToCopy[node].neighbors.append(dfs(nei))

            return ogToCopy[node]       # return the copy node

        return dfs(node)
