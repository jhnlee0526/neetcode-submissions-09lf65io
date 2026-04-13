# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS iteratively
        #   time : O(n) — each node is visited once
        #   space: O(n) — queue and result list grow with number of nodes

        # edge case
        if not root:
            return []

        res = []
        queue = deque([(root, 0)])    # [(node, level), ...]
        while queue:
            qNode, qLevel = queue.popleft()

            if qLevel == len(res):  # If this is the first time we're visiting this level, add a new list
                res.append([])
            res[qLevel].append(qNode.val)

            if qNode.left:
                queue.append([qNode.left, qLevel + 1])
            if qNode.right:
                queue.append([qNode.right, qLevel + 1])
        
        return res
            
