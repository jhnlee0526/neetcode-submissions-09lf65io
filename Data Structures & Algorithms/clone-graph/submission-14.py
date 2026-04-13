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
        #   Time : O(n + e), n = # of nodes, e = # of edges
        #   Space: O(n) hashmap and queue

        # edge case
        if not node:
            return None
        
        ogToClone = {}  # {ogNode : copyNode, ..}
        
        def bfs(curNode):
            q = deque([curNode])    # [node, ..]
            ogToClone[curNode] = Node(curNode.val)

            while q:
                qNode = q.popleft()

                for adjNode in qNode.neighbors:
                    if adjNode not in ogToClone:
                        ogToClone[adjNode] = Node(adjNode.val)
                        q.append(adjNode)
                    ogToClone[qNode].neighbors.append(ogToClone[adjNode])
                
            return ogToClone[curNode]

        return bfs(node)

        ###################
        # DFS recursively
        #   Time : O(n + e), n = # of nodes, e = # of edges
        #   Space: O(n), hashmap and recursion stacks

        ogToClone = {}  # {ogNode: cloneNode, ..}

        def dfs(curNode):
            # base case #1
            if not curNode:
                return None
            # base case #2
            if curNode in ogToClone:
                return ogToClone[curNode]

            ogToClone[curNode] = Node(curNode.val)
            for adjNode in curNode.neighbors:
                ogToClone[curNode].neighbors.append(dfs(adjNode))
            
            return ogToClone[curNode]

        return dfs(node)
        