# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS recursively
        #   Time: O(n) — visit every node once
        #   Space: O(h) — recursion stack depth, where h is the height of the tree
        #       - Worst case: O(n) for a completely skewed tree
        #       - Best case : O(log n) for a balanced tree

        def dfs(node, leftBoundary, rightBoundary):
            if not node:    # base case
                return True

            if not (leftBoundary < node.val < rightBoundary):
                return False

            return dfs(node.left, leftBoundary, node.val) and dfs(node.right, node.val, rightBoundary)

        return dfs(root, float('-inf'), float('inf'))