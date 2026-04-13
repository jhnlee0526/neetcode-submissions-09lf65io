# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS iteratively
        #   Time: O(n) — we visit every node once
        #   Space: O(n) — worst case, all nodes in the queue (e.g., a full binary tree)

        # Edge case: empty tree
        if not root:
            return None
        
        # Initialize queue with root node
        q = deque([root])

        # Process nodes level by level
        while q:
            qNode = q.popleft()

            # Swap left and right children
            qNode.left, qNode.right = qNode.right, qNode.left

            # Add children to queue if they exist
            if qNode.left:
                q.append(qNode.left)
            if qNode.right:
                q.append(qNode.right)
        
        # Return the new root of the inverted tree
        return root

