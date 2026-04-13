"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs recursively + hashmap for the old->new mapping
        #   time : O(n), n = # of nodes
        #   space: O(n)

        oldToNew = {}       # hashmap for the old->new mapping

        def dfs(curNode):   # recursively
            # base case
            if curNode in oldToNew:         # Already created a copy of the current node
                return oldToNew[curNode]    # Return the copy of the current Node

            newNode = Node(curNode.val)             # Create a copy Node of the current node
            oldToNew[curNode] = newNode             # Map the current node with the copy

            for curNei in curNode.neighbors:    # recursively clone all the neighbors of the current node and attach them to the copy node’s neighbors list.
                newNode.neighbors.append(dfs(curNei))
            
            return newNode
    

        return dfs(node) if node else None

        