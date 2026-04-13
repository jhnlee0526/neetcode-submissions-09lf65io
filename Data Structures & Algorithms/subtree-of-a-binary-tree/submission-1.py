# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # dfs recursively
        #   time : O(m * n) in worst case — m = nodes in root, n = nodes in subRoot
        #   space: O(h) — call stack depth of root

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case: an empty subRoot is always a subtree
        if not subRoot:
            return True
        # base case: if root is empty but subRoot isn't, it's not a subtree
        if not root:
            return False
        
        # check if current subtree rooted at 'root' matches 'subRoot'
        if self.isSameTree(root, subRoot):
            return True
        
        # otherwise, check left and right subtrees of 'root'
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # helper function to check if two trees are the same
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        # if both nodes exist and values match, check children
        if (
            p and
            q and
            p.val == q.val
        ):  
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # otherwise, mismatch found
        return False