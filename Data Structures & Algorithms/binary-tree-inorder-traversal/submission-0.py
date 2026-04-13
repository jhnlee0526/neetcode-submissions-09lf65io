# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # dfs recursively to traverse 'inorder'
        # time : O(n), each node is visited once
        # space: O(h) stack + O(n) result
        '''
            h = tree height (worst O(n), balanced O(log n))
            n = storing n values 'res'
        '''
        
        res = []

        def dfs(node):  # recursively
            if not node:
                return
            # inorder traversal : left -> right
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res
        


        
