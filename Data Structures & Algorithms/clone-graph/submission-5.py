"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs iteratively
        #   time : O(N + E) -> O(N), visit each node and edge once
        #   space: O(N), hashmap + queue + cloned nodes

        # edge case
        if not node:
            return None

        ogToCopy = {}   # {ogNode: copyNode, ...}
        q = deque()     # [ogNode, ...]

        def bfs(node):  # iteratively
            q.append(node)
            ogToCopy[node] = Node(node.val)     # Clone the starting node

            while q:
                qNode = q.popleft()
                for nei in qNode.neighbors:     # Traverse all neighbors of the current node
                    if nei not in ogToCopy:
                        ogToCopy[nei] = Node(nei.val)
                        q.append(nei)
                    ogToCopy[qNode].neighbors.append(ogToCopy[nei]) # need to append the cloned version of nei (deep copy)
        
            return ogToCopy[node]

        return bfs(node)

