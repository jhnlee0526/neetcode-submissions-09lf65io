# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS recursively
        #   Time : O(n) — visit every node once
        #   Space: O(h) — recursion stack depth equals tree height
        #   - Worst case: O(n) for a completely skewed tree
        #   - Average case: O(log n) for a balanced tree
        def dfs(pNode, qNode):
            if not pNode and not qNode:
                return True
            if(
                not pNode or 
                not qNode or 
                pNode.val != qNode.val
            ):
                return False

            return dfs(pNode.left, qNode.left) and dfs(pNode.right, qNode.right)
        
        return dfs(p, q)