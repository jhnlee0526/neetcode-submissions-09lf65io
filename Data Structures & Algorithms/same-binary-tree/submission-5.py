# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS iteratively
        #   Time: O(n) — visits each node once
        #   Space: O(n) — queue can hold up to all nodes at the widest level

        # edge case
        if not p and not q:
            return True

        q1, q2 = deque([p]), deque([q])

        while q1 and q2:
            node1, node2 = q1.popleft(), q2.popleft()

            if not node1 and not node2: ##
                continue
            if not node1 or not node2: ##
                return False
            if node1.val != node2.val: ##
                return False

            q1.append(node1.left)
            q2.append(node2.left)
            q1.append(node1.right)
            q2.append(node2.right)

        return not q1 and not q2    ##
