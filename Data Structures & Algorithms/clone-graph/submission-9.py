"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # ✅ DFS recursively
        #   Time : O(N + E) — N = number of nodes, E = number of edges
        #   Space: O(N) — recursion stack + hashmap for visited nodes

        if not node:
            return None

        ogToCopy = {}  # {originalNode : copyNode, ..}

        def dfs(node):
            # base case
            if node in ogToCopy:
                return ogToCopy[node]

            ogToCopy[node] = Node(node.val)

            for nei in node.neighbors:
                # recursively clone neighbors
                ogToCopy[node].neighbors.append(dfs(nei))

            # return the copy node
            return ogToCopy[node]

        return dfs(node)
        

