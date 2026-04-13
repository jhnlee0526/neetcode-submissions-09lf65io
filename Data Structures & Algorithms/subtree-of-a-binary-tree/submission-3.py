# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS recursively
        #   Time: O(m * n) — in worst case, compare subRoot against every subtree of root
        #   Space: O(h) — call stack depth (h = height of root)

        def dfs(node1, node2):
            # base cases
            if not node1:                       # if root is empty but subRoot isn't, it's not a subtree
                return False
            if self.isSametree(node1, node2):   # an empty subRoot is always a subtree
                return True

            return dfs(node1.left, node2) or dfs(node1.right, node2)

        return dfs(root, subRoot)


    # helper function
    def isSametree(self, node1, node2):
        # DFS recursively
        #   Time: O(n) — compares all nodes in subtrees
        #   Space: O(h) — call stack depth

        # base cases
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False

        return self.isSametree(node1.left, node2.left) and self.isSametree(node1.right, node2.right)
