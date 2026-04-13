# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS recursively
        #   Time : O(n) - visit every nodes once
        #   Space: O(h) - worst/skewed O(n), average/balanced O(log n)
        
        self.max_depth = 0
        def dfs(node, cur_depth):
            # base case
            if not node:
                return
            
            self.max_depth = max(self.max_depth, cur_depth)
            dfs(node.left, cur_depth + 1)
            dfs(node.right, cur_depth + 1)

        dfs(root, 1)
        return self.max_depth