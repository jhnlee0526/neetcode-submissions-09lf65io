# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # [easier] BFS iteratively with queue
        #   Time : O(n) — visit each node once
        #   Space: O(n) — for queue and column mapping

        # edge case
        if not root:
            return []
        
        colList = {}                # {col : [node.val, ...], ...}
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


        # -------------------------------------------
        # DFS recursively with sorting
        #   Time : O(n log n) — due to sorting within each column
        #   Space: O(n) — for recursion stack and column mapping

        # edge case: empty tree
        if not root:
            return []

        res = []
        colList = {}                        ## {col : [(node.val, row), ...], ...}
        self.minCol, self.maxCol = 0, 0     # Track column boundaries for ordered output

        def dfs(node, row, col):
            # Base case: null node
            if not node:
                return

            if col not in colList:
                colList[col] = []
            colList[col].append((node.val, row))    # Store (value, row*) for sorting later

            self.minCol = min(self.minCol, col)
            self.maxCol = max(self.maxCol, col)

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)     # Start DFS from root at row=0, col=0

        # Build result by sorting each column's entries by row (top to bottom)
        for col in range(self.minCol, self.maxCol + 1):
            colVals = sorted(colList[col], key=lambda x: x[1])  # sort by row
            res.append([val for val, _ in colVals])
        
        return res

            