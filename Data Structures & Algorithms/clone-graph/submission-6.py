"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS iteratively
        #   Time: O(N + E)
        #       → N = number of nodes
        #       → E = number of edges
        #       → Each node and edge is visited once
        #   Space: O(N)
        #       → HashMap for cloned nodes + queue for BFS

        # base case
        if not node:
            return None

        ogToCopy = {}   # {ogNode : copyNode, ...}
        q = deque()     # [node, ...]

        def bfs(curNode):
            q.append(curNode)
            ogToCopy[curNode] = Node(curNode.val)   # Clone the starting node
            while q:
                qNode = q.popleft()
                for nei in qNode.neighbors:         # Traverse all neighbors of the current node
                    if nei not in ogToCopy:
                        ogToCopy[nei] = Node(nei.val)
                        q.append(nei)
                    # need to append the cloned version of nei (deep copy)
                    ogToCopy[qNode].neighbors.append(ogToCopy[nei])
            return ogToCopy[curNode]

        return bfs(node)