# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS iteratively w/ queue
        #   Time : O(n) - visit every nodes once
        #   Space: O(n) - queue

        # edge case
        if not root:
            return 0
        
        max_depth = 0
        q = deque([(root, 1)])   # [(node, depth), ..]
        while q:
            q_node, q_depth = q.popleft()
            max_depth = max(max_depth, q_depth)
            if q_node.left:
                q.append((q_node.left, q_depth + 1))
            if q_node.right:
                q.append((q_node.right, q_depth + 1))
        
        return max_depth



        #---------------------
        # DFS recursively
        #   Time : O(n) - visit every nodes once
        #   Space: O(h) - worst/skewed O(n), average/balanced O(log n)
        
        self.max_depth = 0
        def dfs(node, cur_depth):
            # base case
            if not node:
                return
            
            self.max_depth = max(self.max_depth, cur_depth)
            dfs(node.left, cur_depth + 1)
            dfs(node.right, cur_depth + 1)

        dfs(root, 1)
        return self.max_depth