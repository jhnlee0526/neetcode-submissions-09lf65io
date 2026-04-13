# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS recursively
        #   time : O(n) — visits each node once
        #   space: O(h) — call stack depth (balanced: O(log n), worst: O(n))
        
        def dfs(n1, n2):
            # base case
            if not n1 and not n2:
                return True
            
            if (
                n1 and 
                n2 and 
                n1.val == n2.val
            ):
                return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)               
            return False
        
        return dfs(p, q)
        