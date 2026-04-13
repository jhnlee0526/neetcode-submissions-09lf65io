"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS iteratively w/ queue
        #   Time : O(N + E), where N = number of nodes, E = number of edges
        #   Space: O(N)

        # edge case
        if not node:
            return None

        ogToCopy = {node : Node(node.val)}       # {ogNode : copyNode, ..}
        q = deque([node])   # [node, ..]

        while q:
            qNode = q.popleft()
            for nei in qNode.neighbors:
                if nei not in ogToCopy:
                    ogToCopy[nei] = Node(nei.val)   # add a new Node for copying 
                    q.append(nei)
                ogToCopy[qNode].neighbors.append(ogToCopy[nei]) # copying neighbors

        return ogToCopy[node]   # return copyNode


        ###########################
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