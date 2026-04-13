# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BFS iteratively w/ queue
        '''
        BFS doesn’t work for finding the k-th smallest element in a BST 
        because it doesn’t respect the BST’s sorted structure, 
        as it traverses the tree level by level.
        '''

        #---------------------
        # DFS recursively (IN-ORDER traversal)
        #   Time : O(n) - visits all nodes in worst case
        #   Space: O(n) - call stack + result list

        res = []
        def dfs(node):
            # base case
            if not node:
                return 

            # IN-ORDER traversal: L -> Node -> R
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res[k - 1]