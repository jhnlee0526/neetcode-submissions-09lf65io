"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Graph: BFS iteratively w/ queue
        #   time : O(n), # of nodes, visits each node once
        #   space: O(n), queue for bfs & hashmap for cloneMap

        # edge case
        if not node:
            return None
        
        cloneMap = {}   # {og node : cloned node, ..}
        q = deque()     # [node, ..]
        
        q.append(node)
        cloneMap[node] = Node(node.val)

        while q:
            qNode = q.popleft()
            for adjNode in qNode.neighbors:
                if adjNode not in cloneMap:     
                    # clone the adjacent node
                    cloneMap[adjNode] = Node(adjNode.val)   
                    q.append(adjNode)

                # clone the neighbors
                cloneMap[qNode].neighbors.append(cloneMap[adjNode])
        
        return cloneMap[node]



        # ---------------------
        # Graph: DFS recursively
        #   time : O(n), # of nodes, visits each node at once 
        #   space: O(n), recursive stacks & hashmap for cloneMap

        # edge case
        if not node:
            return None
        
        cloneMap = {}   # {og node: cloned node, ...}

        def dfs(node):
            # base case
            if node in cloneMap:            # already cloned!
                return cloneMap[node]
            
            cloneMap[node] = Node(node.val)  # clone the current node
            for adjNode in node.neighbors:     # clone the neighbor nodes
                cloneMap[node].neighbors.append(dfs(adjNode))
            
            return cloneMap[node]           # return cloned node   

        return dfs(node)
