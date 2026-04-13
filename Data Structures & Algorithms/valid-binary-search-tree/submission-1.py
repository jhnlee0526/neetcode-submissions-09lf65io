# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS recursively
        #   Time: O(n) — visit each node once
        #   Space: O(h) — call stack depth (h = height of tree)

        def dfs(node, min, max):
            # base case
            if not node:
                return True
            
            if not min < node.val < max:
                return False
            
            return dfs(node.left, min, node.val) and dfs(node.right, node.val, max)

        return dfs(root, float('-inf'), float('inf'))