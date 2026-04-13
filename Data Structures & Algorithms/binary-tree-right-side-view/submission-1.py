# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs iteratively, bottom-up
        #   Time : O(n) — we visit each node once
        #   Space: O(n) — due to the queue and the rightmost dictionary

        if not root:
            return []  # If the tree is empty, there's nothing to see

        # Start with a queue that holds the root node and its depth (level 0)
        queue = deque([(root, 0)])

        # This dictionary will remember the last node we saw at each depth
        rightmost = {}

        # Keep going until there are no more nodes to process
        while queue:
            node, depth = queue.popleft()  # Take the next node and its depth

            # Save or update the value for this depth — the last one we see will be the rightmost
            rightmost[depth] = node.val

            # Add the left child to the queue (if it exists), for the next level
            if node.left:
                queue.append((node.left, depth + 1))

            # Add the right child to the queue (if it exists), for the next level
            if node.right:
                queue.append((node.right, depth + 1))

        # Now build the final list by going through depths in order
        return [rightmost[depth] for depth in sorted(rightmost)]



        
