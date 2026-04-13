# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS iteratively
        #   Time: O(n) — each node is visited once
        #   Space: O(n) — in the worst case, the queue holds all nodes at the widest level

        # edge case
        if not root:
            return []

        res = []
        
        q = deque([(root, 0)]) # [(node, level), ...]
        while q:
            qNode, qLevel = q.popleft()

            if qLevel == len(res):   # check if it's the first time visiting the level
                res.append([])
            res[qLevel].append(qNode.val)

            if qNode.left:
                q.append((qNode.left, qLevel + 1))
            if qNode.right:
                q.append((qNode.right, qLevel + 1))

        return res
            