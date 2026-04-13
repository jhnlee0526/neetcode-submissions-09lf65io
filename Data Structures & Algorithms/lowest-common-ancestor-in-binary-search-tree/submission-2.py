# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BFS iteratively with queue (queue use is not necessary)
        #   time : O(h) - worst O(n) skewed tree. average O(log n) balanced tree
        #   space: O(h)
        
        # base case
        if not root:
            return None

        queue = deque([root])
        while queue:
            qNode = queue.popleft()
            if qNode.val > p.val and qNode.val > q.val:
                queue.append(qNode.left)
            elif qNode.val < p.val and qNode.val < q.val:
                queue.append(qNode.right)
            else:
                return qNode
        
        