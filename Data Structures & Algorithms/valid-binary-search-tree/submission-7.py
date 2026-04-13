# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS iteratively w/ queue
        #   Time : O(n)
        #       - each node visited once
        #   Space: O(n)
        #       - queue holds up to n nodes in worst case

        # egde case
        if not root:
            return True
        
        # [(leftBoundary, node, rightBoundary), ..]
        q = deque([(float('-inf'), root, float('inf')),]) 
        while q:
            leftBoundary, q_node, rightBoundary = q.popleft()

            if not leftBoundary < q_node.val < rightBoundary:
                return False
            
            if q_node.left:
                q.append((leftBoundary, q_node.left, q_node.val))
            if q_node.right:
                q.append((q_node.val, q_node.right, rightBoundary))

        return True


        #------------------------
        # DFS recursively
        #   Time : O(n)
        #   Space: O(h) — recursion stack depth, where h is the height of the tree
        #       - Worst case: O(n) for a completely skewed tree
        #       - Best case : O(log n) for a balanced tree

        def dfs(leftBoundary, node, rightBoundary):
            # base cases
            if not node:
                return True
            if not leftBoundary < node.val < rightBoundary:
                return False

            return (
                dfs(leftBoundary, node.left, node.val) and 
                dfs(node.val, node.right, rightBoundary)
            )

        return dfs(float('-inf'), root, float('inf'))