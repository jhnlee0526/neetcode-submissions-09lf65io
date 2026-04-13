# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Recursive DFS approach to build binary tree from preorder and inorder traversals
        #   Time : O(n^2) — due to slicing and index lookup in each recursive call
        #   Space: O(n) — recursion stack + cumulative cost of list slicing

        # Base case: no nodes to construct
        if not preorder or not inorder:
            return None

        # First element in preorder is the root of the current subtree
        root = TreeNode(preorder[0])

        # Find the root's index in inorder to divide left and right subtrees
        mid = inorder.index(preorder[0])  # O(n) time per call

        # Build left subtree using:
        # - preorder[1 : mid + 1] → elements corresponding to left subtree
        # - inorder[: mid]        → elements before root in inorder
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])

        # Build right subtree using:
        # - preorder[mid + 1 :]   → elements after left subtree in preorder
        # - inorder[mid + 1 :]    → elements after root in inorder
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        # Return the constructed subtree rooted at 'root'
        return root

        