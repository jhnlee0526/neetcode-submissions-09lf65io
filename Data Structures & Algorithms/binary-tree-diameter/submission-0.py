# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs recursively 
        #   time : O(n) - visits each node onces
        #   space: O(h) - worst O(n), balanced O(log n)

        maxLen = 0

        def dfs(node): # recursively
            nonlocal maxLen
            
            # Base case: null node contributes 0 to height
            if not node:
                return 0

            # Recursively compute the height of left and right subtrees
            leftLen = dfs(node.left)
            rightLen = dfs(node.right)

            # Update the diameter(maxLen) at this node
            maxLen = max(maxLen, leftLen + rightLen)

            # Return the height of this subtree to the parent
            return 1 + max(leftLen, rightLen)

        dfs(root)
        return maxLen