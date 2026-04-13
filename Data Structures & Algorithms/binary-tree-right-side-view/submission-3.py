# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # DFS recursively (WITHOUT levels)*
        '''Traverse RIGHT before left, and record the first node seen at each depth.'''
        #   Time : O(n) — visit each node once
        #   Space: O(h) — recursion stack, h = height of tree

        res = []    # [node1, node2, ...]

        def dfs(node, depth):
            # base case
            if not node:
                return

            # First node at this depth — must be the RIGHTMOST due to traversal order
            if depth == len(res):   # once right node is added, left node can't be add due to the if statement
                res.append(node.val)

            # Traverse RIGHT FIRST to prioritize rightmost nodes
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
