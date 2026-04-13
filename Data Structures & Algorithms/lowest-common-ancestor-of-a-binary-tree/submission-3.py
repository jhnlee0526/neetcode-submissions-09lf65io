# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs recursively
        ## time : O(n) - visit each node once
        ## space: O(n) - due to the recursive call stack, worst case for skewed tree is O(n)

        def dfs(node):
            # base case
            if (
                not node or
                node == p or
                node == q
            ):
                return node            # found it!

            leftNode = dfs(node.left)
            rightNode = dfs(node.right)

            if leftNode and rightNode: # there is a split.
                return node            # found it!
            
            return leftNode or rightNode

        return dfs(root) ##
