# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # dfs recursively to traverse 'preorder'
        #   time : O(n), each node is visited once
        #   space: O(h) + O(n)
        '''
            h = tree height (worst O(n), balanced O(log n)) : 'stack'
            n = storing n values : 'result'
        '''

        res = []

        def dfs(node): # recursively
            # base case
            if not node:
                return

            # preorder traversal: root -> children(left -> right)
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res