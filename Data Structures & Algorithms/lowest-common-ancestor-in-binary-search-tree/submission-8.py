# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BFS iteratively w/ queue
        #   Time : O(h)
        #       - h = height of tree
        #       - O(log n) for balanced BST, O(n) for skewed
        #   Space: queue holds at most one node at a time

        # edge case
        if not root:
            return None
        
        queue = deque([root])   # [node, ..]
        while queue:
            q_node = queue.popleft()
            
            if q_node.val < p.val and q_node.val < q.val:
                queue.append(q_node.right)
            elif q_node.val > p.val and q_node.val > q.val:
                queue.append(q_node.left)
            else:
                return q_node


        #--------------------------
        # DFS recursively
        #   Time : O(h)
        #       - h = height of tree
        #       - O(log n) for balanced BST, O(n) for skewed
        #   Space: O(h)
        #       - call stack depth

        def dfs(node):
            # base case
            if not node:
                return None
            
            if node.val < p.val and node.val < q.val:
                return dfs(node.right)

            elif node.val > p.val and node.val >q.val:
                return dfs(node.left)

            else:   #SPLIT! node.val > p.val and node.val < q.val
                return node
        
        return dfs(root)
                