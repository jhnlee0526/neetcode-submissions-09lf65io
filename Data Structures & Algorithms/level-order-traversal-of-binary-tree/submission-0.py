# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # dfs recursively
        #   time : O(n) — we visit each node exactly once
        #   space: O(h) — recursion stack, where h is the height of the tree

        res = []

        def dfs(node, level):   # recursively
            if not node:                    # base case
                return

            if level == len(res):           # If this is the first time we're visiting this level, add a new list
                res.append([])
            res[level].append(node.val)     # Append the node's value to its level list

            # Recurse left and right, increasing the level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res