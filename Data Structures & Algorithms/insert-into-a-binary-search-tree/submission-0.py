# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # dfs recursively
        #   time : O(h) — h is the height of the tree
        #                   - Balanced BST: O(log n)
        #                   - Skewed BST: O(n)
        #   space: O(h) — recursion stack depth

        # base case: insert new node here
        if not root:
            return TreeNode(val)

        if val < root.val:  # recurse into left subtree
            root.left = self.insertIntoBST(root.left, val)
        
        else:               # recurse into right subtree
            root.right = self.insertIntoBST(root.right, val)

        # return unchanged root after insertion
        return root