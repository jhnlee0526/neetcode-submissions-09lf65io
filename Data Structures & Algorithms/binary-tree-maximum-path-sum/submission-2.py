# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize result to negative infinity to handle trees with all negative values
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0  # Null nodes contribute 0 to path sum

            # Recursively compute 'max path sum' from left and right subtrees
            leftMax = max(dfs(node.left), 0)   # Only include if positive
            rightMax = max(dfs(node.right), 0) # Only include if positive

            # Update 'global max' if the current node forms a higher path sum
            self.res = max(self.res, node.val + leftMax + rightMax)

            # Return 'max gain' if continuing the path through parent
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return self.res  # Final result: maximum path sum in the tree