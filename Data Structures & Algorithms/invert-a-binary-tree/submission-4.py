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

        if not root:
            return None

        def bfs(node):
            q = deque([node])
            while q:
                qn = q.popleft()
                qn.left, qn.right = qn.right, qn.left
                if qn.left:
                    q.append(qn.left)
                if qn.right:
                    q.append(qn.right)
        bfs(root)

        return root
            
