# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS recursively: 'Optimized' in-order traversal
        #   Time: O(n) — visit each node once
        #   Space: O(h) — call stack depth (h = height of tree)
        
        self.count = 0
        self.res = None

        def dfs(node):
            # base case
            if not node or self.res:
                return
            
            # in-order traversal: left -> root -> right
            dfs(node.left)
            
            self.count += 1
            if self.count == k:
                self.res = node.val
            
            dfs(node.right)

        dfs(root)
        return self.res