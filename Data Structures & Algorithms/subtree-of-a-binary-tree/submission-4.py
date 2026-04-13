# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # BFS iteratively
        # Time: O(n * m) — for each node in `root`, we may compare up to m nodes in `subRoot`
        # Space: O(w) — where w is the max width of the `root` tree (queue size)
        if not root:    # edge case
            return False
        
        q = deque([root])
        while q:
            qNode = q.popleft()
            if self.isSameTree(qNode, subRoot):
                return True
            if qNode.left:
                q.append(qNode.left)
            if qNode.right:
                q.append(qNode.right)
        return False

        #########################
        # DFS recursively
        # Time: O(m * n) — in the worst case, for each of the "n" nodes in `root`, 
        #                  we may compare up to "m" nodes in `subRoot` via isSameTree
        # Space: O(h) — recursion stack depth for traversing `root`, where h is the height of `root`
        
        def dfs(node1, node2):
            # base cases
            if not node1:   # if root is empty but subRoot isn't, it's not a subtree
                return False
            if self.isSameTree(node1, node2):
                return True
            return dfs(node1.left, node2) or dfs(node1.right, node2)
        
        return dfs(root, subRoot)


    # helper function
    def isSameTree(self, root1, root2) -> bool:
        # DFS recursively
        #   Time : O(m) — compare all nodes in subtrees rooted at root1 and root2
        #   Space: O(m) — recursion stack depth for subtree comparison
        
        # base cases
        if not root1 and not root2:
            return True
        if(
            not root1 or 
            not root2 or 
            root1.val != root2.val
        ):
            return False
        
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)