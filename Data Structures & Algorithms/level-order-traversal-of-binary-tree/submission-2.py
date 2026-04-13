# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS recursively
        #   time :
        #   space:

        res = []
        def dfs(node, level):
            if not node:    # base case
                return
            
            if level == len(res):   # check if it's first time visiting the level
                res.append([])
            res[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return res