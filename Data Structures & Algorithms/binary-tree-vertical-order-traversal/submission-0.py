# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS iteratively with queue
        #   Time : O(n) — visit each node once
        #   Space: O(n) — for queue and column mapping

        if not root:
            return []
        
        colList = {}                # {col : [node, ...], ...}
        minCol, maxCol = 0, 0       # Column boundaries, for iteration at the end
        q = deque([(root, 0)])      # [(node, col), ...]
        
        while q:
            qNode, qCol = q.popleft()
            
            if qCol not in colList:
                colList[qCol] = []
            colList[qCol].append(qNode.val)

            minCol = min(minCol, qCol)
            maxCol = max(maxCol, qCol)

            # Add left and right children to queue with updated column indices
            if qNode.left:
                q.append((qNode.left, qCol - 1))
            if qNode.right:
                q.append((qNode.right, qCol + 1))

        return [colList[col] for col in range(minCol, maxCol + 1)]
            