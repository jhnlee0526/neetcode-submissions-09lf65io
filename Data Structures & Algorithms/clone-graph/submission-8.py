"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # ✅ BFS iteratively with queue
        #   Time : O(N + E) — N = nodes, E = edges
        #   Space: O(N) — for hashmap and queue

        if not node:
            return None

        ogToCopy = {node: Node(node.val)}  # {originalNode : copyNode, ..}
        q = deque([node])                  # [node, ..]

        while q:
            qNode = q.popleft()

            for nei in qNode.neighbors:
                if nei not in ogToCopy:
                    q.append(nei)
                    ogToCopy[nei] = Node(nei.val)
                ## Append the cloned neighbor to the cloned node's neighbor list
                ogToCopy[qNode].neighbors.append(ogToCopy[nei])

        return ogToCopy[node]
        

