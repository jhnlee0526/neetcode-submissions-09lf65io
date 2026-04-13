# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs recursively
        #   time : O(n) — visit each node once
        #   space: O(h) — recursion stack, h = height of tree

        levels = [] # [[nodeLeft, nodeRight], ...]
        
        def dfs(node, depth): # recursively
            # base case
            if not node:
                return
            
            # If this is the first time we're visiting this depth, add the node's value
            if depth == len(levels):
                levels.append([])
            levels[depth].append(node.val)
            
            # Traverse right first to prioritize rightmost nodes
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return [eachLevel[-1] for eachLevel in levels] # [left, right]
