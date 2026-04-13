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
        #   Time: O(N + E)
        #       → N = number of nodes
        #       → E = number of edges
        #       → Each node and edge is visited once
        #   Space: O(N)
        #       → HashMap for cloned nodes + recursion stack
        
        # base case
        if not node:
            return None

        ogToCopy = {}   # {ogNode : copyNode, ...}

        def dfs(curNode):
            # edge case : if already exist, return it
            if curNode in ogToCopy:
                return ogToCopy[curNode]
            
            # add the copy node to the map
            ogToCopy[curNode] = Node(curNode.val)

            # copy neighbors
            for nei in curNode.neighbors:
                ogToCopy[curNode].neighbors.append(dfs(nei))

            # return the copy node
            return ogToCopy[curNode]                    
                
        return dfs(node)

        