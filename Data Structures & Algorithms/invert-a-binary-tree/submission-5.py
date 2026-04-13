# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS recursively
        #   Time : O(n) — we visit every node once
        #   Space: O(h) — recursion stack depth equals the height of the tree
        #   - Worst case (skewed tree): O(n)
        #   - Best/average case (balanced tree): O(log n)
        
        def dfs(node):
            if not node: # base case
                return
            node.left, node.right = node.right, node.left   # swap left and right           
            dfs(node.left)
            dfs(node.right)
            return node

        return dfs(root)
        
