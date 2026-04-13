# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs recursively
        #   time : O(n) - visits each node once
        #   space: O(h) - worst O(n), balanced O(log n)

        def dfs(node):  # recursively
            # base case
            if not node:                                # height of empty subtree
                return 0

            leftHeight = dfs(node.left)
            if leftHeight == -1: 
                return -1                               # left subtree unbalanced

            rightHeight = dfs(node.right)
            if rightHeight == -1: 
                return -1                               # right subtree unbalanced

            if abs(leftHeight - rightHeight) > 1:
                return -1                               # current node unbalanced

            return max(leftHeight, rightHeight) + 1     # return height

        return dfs(root) != -1