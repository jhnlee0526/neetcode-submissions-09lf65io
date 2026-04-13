# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS recursively
        #   time : O(n) - visits each node onces
        #   space: O(h) - worst O(n), balanced O(log n)
        
        # edge case
        if not root:
            return 0

        maxDepth = 0
        def dfs(node, curDepth):
            nonlocal maxDepth

            # base case
            if not node:
                return

            maxDepth = max(maxDepth, curDepth)
            dfs(node.left, curDepth + 1)
            dfs(node.right, curDepth + 1)
        
        dfs(root, 1)    # starting from 1 for the depth
        return maxDepth
        
