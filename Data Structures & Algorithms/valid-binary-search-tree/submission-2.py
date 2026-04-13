# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS iteratively with queue
        #   Time : O(n) — each node is visited once
        #   Space: O(n) — in the worst case, the queue holds all nodes

        if not root:
            return True
        
        q = deque([(root, float('-inf'), float('inf'))]) # [(node, min, max), ..]
        while q:
            qNode, qMin, qMax = q.popleft()
            
            if not qMin < qNode.val < qMax:
                return False

            if qNode.left:
                q.append((qNode.left, qMin, qNode.val))
            if qNode.right:
                q.append((qNode.right, qNode.val, qMax))
        
        return True