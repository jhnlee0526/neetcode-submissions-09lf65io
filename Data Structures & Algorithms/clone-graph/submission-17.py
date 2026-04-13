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
        #   Time: O(N + E)
        #       → N = number of nodes
        #       → E = number of edges
        #       → Each node and edge is visited once
        #   Space: O(N)
        #       → HashMap for cloned nodes + queue for BFS
        
        # edge case
        if not node:
            return None

        cloneMap = {}   # {og node : cloned node, ..}
        q = deque()     # [node, ..]
        
        def bfs(node):
            q.append(node)
            cloneMap[node] = Node(node.val) #clone the current node

            while q:
                qNode = q.popleft()
                for adjNode in qNode.neighbors:
                    if adjNode not in cloneMap:
                        cloneMap[adjNode] = Node(adjNode.val)   # clone the adjacent node
                        q.append(adjNode)
                    # append the cloned version of nei (deep copy)
                    cloneMap[qNode].neighbors.append(cloneMap[adjNode])
            return cloneMap[node]

        return bfs(node)
        
        
        # ---------
        # dfs recursively 
        #   time : O(n), # of nodes
        #   space: O(n)
        
        #edge case
        if not node:
            return None

        cloneMap = {}   # {og node : cloned node, ..}

        def dfs(node):
            if node in cloneMap:    # base case 
                return cloneMap[node]
            
            # clone the current node
            cloneMap[node] = Node(node.val)
            # clone the adjacent nodes by dfs the each adjnode recursively
            for adjNode in node.neighbors:
                cloneMap[node].neighbors.append( dfs(adjNode) )
            
            return cloneMap[node]

        return dfs(node)
            
