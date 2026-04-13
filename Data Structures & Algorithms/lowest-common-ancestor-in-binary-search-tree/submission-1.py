# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # DFS recursively
        #   time : O(h) - worst O(n) skewed tree. average O(log n) balanced tree
        #   space: O(h)

        def dfs(node, p, q):
            # base case
            if not node:
                return None
            
            if node.val > p.val and node.val > q.val:   # Both q and p smaller than the current node
                return dfs(node.left, p, q)
            elif node.val < p.val and node.val < q.val: # both q and p larger than the current node
                return dfs(node.right, p, q)
            else:                                       # When p and q split -> LCA
                return node
            
        return dfs(root, p, q)