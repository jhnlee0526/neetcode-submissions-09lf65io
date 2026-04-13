# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS recursively
        #   Time : O(n) - visit every nodes once
        #   Space: O(h) - worst/skewed O(n), avg/balanced O(log n)
        def dfs(node1, node2):
            # base cases
            if not node1:
                return False
            if self.isSametree(node1, node2):
                return True
            
            return dfs(node1.left, node2) or dfs(node1.right, node2)

        return dfs(root, subRoot)
    
    # helper function
    def isSametree(self, p, q):
        # DFS recursively
        #   Time : O(n) - visit every nodes once
        #   Space: O(h) - worst/skewed O(n), avg/balanced O(log n)
        def dfs(node1, node2):
            # base cases
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
        return dfs(p, q)
    