# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # DFS recursively
        #   Time: O(h) — where h is the height of the tree
        #       - Worst case: O(n) for a completely skewed tree
        #       - Best/average case: O(log n) for a balanced BST
        #   Space: O(h) — recursion stack depth
        
        def dfs(node):
            if not node:    # base case
                return None

            # traversing
            if(
                node.val > p.val and
                node.val > q.val
            ):
                return dfs(node.left)
            if (
                node.val < p.val and
                node.val < q.val
            ):
                return dfs(node.right)
            
            # This is the split point — LCA
            return node

        return dfs(root)

