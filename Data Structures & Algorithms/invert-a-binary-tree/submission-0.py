# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs recursively
        #   Time : O(n)     – visit each node once.
        #   Space: O(h)     – recursion stack 
        '''h = tree height; worst O(n), balanced O(log n)).'''

        def dfs(node): # recursively
            # base case
            if not node:
                return
            # swap left <-> right
            node.left, node.right = node.right, node.left
            # recurse on children
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root