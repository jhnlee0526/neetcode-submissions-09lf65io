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
        #   Space: O(h) — recursion stack, h = height of tree

        def dfs(min_val, node, max_val):    # recursively
            if not node:
                return True

            # Current node must be strictly between min and max bounds
            if not (min_val < node.val < max_val):
                return False

            # Left subtree: max bound becomes current node
            # Right subtree: min bound becomes current node
            return dfs(min_val, node.left, node.val) and dfs(node.val, node.right, max_val)

        return dfs(float('-inf'), root, float('inf'))
        

        
        