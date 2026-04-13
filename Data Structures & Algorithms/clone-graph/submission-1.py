"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs recursively + hashmap for the original-copy mapping
        #   time : O(n), n : # of nodes
        #   space: O(n)

        ogToCopy = {}   # {ogNode : copyNode, }
        
        def dfs(curNode): # recursively
            # base case
            if curNode in ogToCopy:         # already finishing copying the current node
                return ogToCopy[curNode]    # return the copy node
            
            # create a copy node
            copyNode = Node(curNode.val)
            ogToCopy[curNode] = copyNode    # mapping

            # copy neighbors by dfs the each nei recursively
            for nei in curNode.neighbors:
                copyNode.neighbors.append(dfs(nei))

            return copyNode
        
        return dfs(node) if node else None