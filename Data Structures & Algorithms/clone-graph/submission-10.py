"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS recursively
        #   Time : O(N + E), where N = number of nodes, E = number of edges
        #   Space: O(N) for hashmap and recursion stack

        ogToCopy = {}   # {ogNode : copyNode, ...}
        
        def dfs(curNode):
            # base cases
            if not curNode:
                return None
            if curNode in ogToCopy:     # already exist -> return the copyNode
                return ogToCopy[curNode]
            
            ogToCopy[curNode] = Node(curNode.val)   # add a new Node for copying

            for nei in curNode.neighbors:           # copying the neighbors
                ogToCopy[curNode].neighbors.append(dfs(nei))

            return ogToCopy[curNode]                # return the copyNode
        
        return dfs(node)