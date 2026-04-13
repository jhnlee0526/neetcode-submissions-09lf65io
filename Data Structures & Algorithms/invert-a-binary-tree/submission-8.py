# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS recursively 
        #   Time : O(n) - visits every nodes
        #   Space: O(h) - O(n) Worst/skewed, O(log n) average/balaced

        # edge / base case
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        

        #---------------------------------------
        # BFS iteratively w/ queue
        #   Time : O(n) - visit every nodes
        #   Space: O(n) - queue
        
        # edge case
        if not root:
            return None

        q = deque([root]) # [node1, ..]
        while q:
            qNode = q.popleft()
            qNode.left, qNode.right = qNode.right, qNode.left
            if qNode.right:
                q.append(qNode.right)
            if qNode.left:
                q.append(qNode.left)
            
        return root


