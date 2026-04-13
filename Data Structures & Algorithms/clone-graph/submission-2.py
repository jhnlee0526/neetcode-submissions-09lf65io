"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # (*dfs is prefered) bfs iteratively with queue + hashmap for the original-copy mapping
        #   time : O(N + E) -> O(N), visit each node and edge once
        #   space: O(N), hashmap + queue + cloned nodes

        if not node: # edge case
            return None

        ogToCopy = {}   # {ogNode : copyNode, }

        def bfs(curNode): # iteratively
            q = deque([curNode])                        # queue: [curNode, ... ]
            copyNode = Node(curNode.val)                # create a copy and map it
            ogToCopy[curNode] = copyNode

            while q:
                qNode = q.popleft()
                for nei in qNode.neighbors:
                    if nei not in ogToCopy:
                        q.append(nei)                   # queue
                        ogToCopy[nei] = Node(nei.val)   # create a copy and map it
                    
                    ogToCopy[qNode].neighbors.append(ogToCopy[nei])
            
            return ogToCopy[curNode]
        
        return bfs(node)