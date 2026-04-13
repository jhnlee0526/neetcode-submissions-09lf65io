# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS recursively
        #   Time : O(n)
        #       - visit each node once
        #   Space: O(n)
        #       - queue holds up to n nodes in worst case
        #       - result list also stores all node values

        # edge case
        if not root:
            return []

        res = []
        q = deque([root])   # [node, ..]
        while q:
            level = []
            for _ in range(len(q)):
                q_node = q.popleft()
                level.append(q_node.val)

                if q_node.left:
                    q.append(q_node.left)
                if q_node.right:
                    q.append(q_node.right)
            
            res.append(level)

        return res
                    