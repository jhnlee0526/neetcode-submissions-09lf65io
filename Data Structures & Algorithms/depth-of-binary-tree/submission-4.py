# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS iteratively
        #   Time : O(n) — we visit each node once
        #   Space: O(n) — in the worst case, the queue holds all nodes at the widest level

        if not root:    # edge case
            return 0

        maxDepth = 0
        q = deque([(root, 1),])  # [(node, depth), ..]
        while q:
            qNode, qDepth = q.popleft()
            maxDepth = max(maxDepth, qDepth)
            if qNode.left:
                q.append((qNode.left, qDepth + 1))
            if qNode.right:
                q.append((qNode.right, qDepth + 1))
        
        return maxDepth

        ##############################
        # DFS recursively
        #   Time: O(n) — visit every node once
        #   Space: O(h) — recursion stack depth equals tree height
        #   - Worst case (skewed tree): O(n)
        #   - Best/average case (balanced tree): O(log n)

        self.maxDepth = 0
        def dfs(node, curDepth):
            if not node:    # base case
                return
            self.maxDepth = max(self.maxDepth, curDepth)    # update max depth
            dfs(node.left, curDepth + 1)
            dfs(node.right, curDepth + 1)

        dfs(root, 1)    ## start depth at 1 (root level)
        return self.maxDepth