# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In-order DFS traversal
        #   Time : O(n) — visit each node once
        #   Space: O(n) — store up to n node values in res

        res = []
        def dfs(node):  # recursively
            # base case
            if not node:
                return
            
            # in-order traversal: left -> root -> right
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res[k - 1]