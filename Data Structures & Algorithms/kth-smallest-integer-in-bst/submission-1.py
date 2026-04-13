# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS recursively: 'In-order' traversal
        #   Time: O(n) — visit each node once
        #   Space: O(n) — store all node values + call stack depth
        
        treeVals = []    # [node.val, ...]

        def dfs(node):
            # base case
            if not node:
                return
            # 'in-order' traversal: left -> root -> right
            dfs(node.left)
            treeVals.append(node.val)
            dfs(node.right)

        dfs(root)
        return treeVals[k - 1]   # 1-indexed