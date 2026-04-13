# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs recursively
        #   time : O(n) — visits each node once
        #   space: O(h) — call stack depth (balanced: O(log n), worst: O(n))

        def dfs(node1, node2): # recursively
            # base case
            if not node1 and not node2:
                return True
            
            if(
                node1 and
                node2 and
                node1.val == node2.val
            ):
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)    # both nodes exist and values match — check children
            return False    # otherwise mismatch found
        
        return dfs(p, q)
