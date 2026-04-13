# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS iteratively
        #   Time: O(n) — we visit each node once
        #   Space: O(n) — in the worst case, the queue holds all nodes at the widest level

        # Edge case: empty tree has depth 0
        if not root:
            return 0
        
        maxDepth = 0
        q = deque([(root, 1)])  # Queue holds tuples of (node, current depth)

        while q:
            node, depth = q.popleft()
            maxDepth = max(maxDepth, depth)

            # Add children to the queue with incremented depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        return maxDepth       
