# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs recursively
        #   time : O(n), # of nodes
        #   space: O(h), recusion stack: tree height (worst O(n), balanced O(log n))

        def dfs(node):
            # base case
            if not node:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
