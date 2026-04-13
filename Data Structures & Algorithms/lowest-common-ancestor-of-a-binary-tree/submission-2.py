# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs recursively
        ## Time: O(n) → we visit each node once
        ## Space: O(n) → due to recursive call stack, worst case for skewed tree
        
        def dfs(node):
            # base case
            if (
                not node or
                node == p or
                node == q
            ):
                return node         # Report what we found

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:      # this is where the SPLIT is -> LCA
                return node         # found the LCA!
            
            return left or right    # Only one node found, bubble it (keep doing recursion)

        return dfs(root)