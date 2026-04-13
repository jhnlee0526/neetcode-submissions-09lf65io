# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # DFS recursively
        #   Time : O(h)
        #       - h = height of tree
        #       - O(log n) for balanced BST, O(n) for skewed
        #   Space: O(h)
        #       - call stack depth

        def dfs(node):
            # base case
            if not node:
                return None
            
            if node.val < p.val and node.val < q.val:
                return dfs(node.right)

            elif node.val > p.val and node.val >q.val:
                return dfs(node.left)

            else:   #SPLIT! node.val > p.val and node.val < q.val
                return node
        
        return dfs(root)
                