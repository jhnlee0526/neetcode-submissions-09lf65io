# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs recursively
        #   time : O(n) - visits each node onces
        #   space: O(h) - worst O(n), balanced O(log n)

        maxDep = 0
        def dfs(node, level): # recursively
            nonlocal maxDep

            # base case
            if not node:
                return
            
            maxDep = max(maxDep, level)
            # recursion on children
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            

        dfs(root, 1) # starting from level 1
        return maxDep