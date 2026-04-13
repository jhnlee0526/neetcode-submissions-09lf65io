# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # dfs recursively
        #   time : 
        #   space:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        if not subRoot:
            return True
        if not root:
            return False
        
        # check if those are the same
        if self.isSameTree(root, subRoot):
            return True
        # if not the same trees, check if it's subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # helper function to check if two trees are the same
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if (
            p and
            q and
            p.val == q.val
        ):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False