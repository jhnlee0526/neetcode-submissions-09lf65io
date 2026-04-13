# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # BFS iteratively
        # #   Time : O(n) — visit every node once
        # #   Space: O(w) — where w is the maximum width of the tree
        # #       - Worst case: O(n) if the bottom level has ~n/2 nodes (perfectly balanced tree)
        # #       - Best case : O(1) if the tree is completely skewed (only one node per level)

        # if not root:    # edge case
        #     return []
        
        # res = []
        # q = deque([root])
        # while q:
        #     level = []
        #     for _ in range(len(q)):
        #         qNode = q.popleft()
        #         level.append(qNode.val)
        #         if qNode.left:
        #             q.append(qNode.left)
        #         if qNode.right:
        #             q.append(qNode.right)
        #     res.append(level)
        
        # return res

        ######################
        # DFS recursively
        #   Time : O(n) — visit every node once
        #   Space: O(n) — worst case for a completely skewed tree (recursion depth = n, and res holds n levels)

        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append([])  # start a new level
            res[depth].append(node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 0)
        return res

            