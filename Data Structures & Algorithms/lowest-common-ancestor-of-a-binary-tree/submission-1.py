# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs recursively
        ## time : O(n)
        ## space: O(n)

        # base case
        if (
            not root or
            root == p or
            root == q
        ):  
            return root     # 🎯 Found one of the nodes, or reached the end

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:      # This is where p & q splits! -> LCA
            return root         # 📌 Found p in one side and q in the other
        
        return left or right    # 🛣️ Only one node found, bubble it (keep doing recursion)