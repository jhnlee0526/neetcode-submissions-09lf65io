# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dfs recursively
        #   time : O(h)
        #       - In a balanced BST, height h = log n → O(log n) time.
        #       - In a skewed BST, height h = n → O(n) time.
        #   space: O(h)
        #       - Balanced BST → O(log n) space.
        #       - Skewed BST → O(n) space.

        def dfs(node, p, q):
            if not node:
                return None
            
            # both nodes are in the left subtree
            if p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q)
            
            # both nodes are in the right subtree
            if p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)
            
            # !! nodes split or match — current node is LCA
            return node

        return dfs(root, p, q)
