# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs recursively
        #   Time: O(n) — visit each node once
        #   Space: O(h) — recursion stack, h = height of tree

        def dfs(node, maxVal):  # recursively
            if not node:
                return 0

            cnt = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            # cnt = 0
            # if node.val >= maxVal:
            #     cnt += 1
            #     maxVal = max(maxVal, node.val)
            
            cnt += dfs(node.left, maxVal)
            cnt += dfs(node.right, maxVal)
            
            return cnt

        return dfs(root, root.val)