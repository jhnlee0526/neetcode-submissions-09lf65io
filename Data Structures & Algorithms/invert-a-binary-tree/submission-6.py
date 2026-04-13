# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS iteratively
        #   Time: O(n) — we visit every node once to swap its children
        #   Space: O(n) — queue holds up to one full level of the tree at a time

        if not root:  # edge case
            return None

        q = deque([root])
        while q:
            qNode = q.popleft()
            qNode.left, qNode.right = qNode.right, qNode.left   # Swap left and right
            if qNode.left:
                q.append(qNode.left)
            if qNode.right:
                q.append(qNode.right)

        return root
        
        ###################################
        # DFS recursively
        #   Time : O(n) — we visit every node once
        #   Space: O(h) — recursion stack depth equals the height of the tree
        #   - Worst case (skewed tree): O(n)
        #   - Best/average case (balanced tree): O(log n)
        
        def dfs(node):
            if not node: # base case
                return
            node.left, node.right = node.right, node.left   # swap left and right           
            dfs(node.left)
            dfs(node.right)
            return node

        return dfs(root)
        
