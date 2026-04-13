# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS iteratively
        # Time: O(n) — visit every node once and compare values
        # Space: O(n) — each queue can hold up to n/2 nodes in the worst case (bottom level of a balanced tree)
        
        if not p and not q: # edge case
            return True

        q1, q2 = deque([p]), deque([q])
        while q1 and q2:
            q1Node, q2Node = q1.popleft(), q2.popleft()

            if not q1Node and not q2Node:   ##
                continue
            if not q1Node or not q2Node:
                return False
            if q1Node.val != q2Node.val:
                return False

            q1.append(q1Node.left)  # left
            q2.append(q2Node.left)
            q1.append(q1Node.right) # right
            q2.append(q2Node.right)

        return not q1 and not q2    ## ensure both queues are exhausted simultaneously


        ##########################
        # DFS recursively
        #   Time : O(n) — visit every node once
        #   Space: O(h) — recursion stack depth equals tree height
        #   - Worst case: O(n) for a completely skewed tree
        #   - Average case: O(log n) for a balanced tree
        def dfs(pNode, qNode):
            if not pNode and not qNode:
                return True
            if(
                not pNode or 
                not qNode or 
                pNode.val != qNode.val
            ):
                return False

            return dfs(pNode.left, qNode.left) and dfs(pNode.right, qNode.right)
        
        return dfs(p, q)