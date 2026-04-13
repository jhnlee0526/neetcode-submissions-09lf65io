# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs recursively
        ## time : O(n) , there are n nodes in the tree, and you visit each node once during the depth-first search.
        ## space: O(h) , h is the height of the tree. Worst case (linked list): O(n) & Best case (balanced tree): O(log n)
        
        LCA = None  # 🎯 This will store the answer once we find it

        def dfs(node):
            nonlocal LCA
            # 🛑 Base case: If we hit a dead end or already found LCA
            if not node or LCA:
                return [False, False]  # False for p and q

            # 🔍 Search left & right subtree
            left = dfs(node.left)
            right = dfs(node.right)

            # 🧠 Check if current node is p or q, or they exist in left/right subtrees
            foundP = left[0] or right[0] or (node == p)
            foundQ = left[1] or right[1] or (node == q)

            # 🎯 If both found and we haven't set LCA yet, lock it in
            if foundP and foundQ and not LCA:
                LCA = node

            # ⬆️ Return whether p or q are found in this subtree
            return [foundP, foundQ]

        # 🚀 Start DFS from root
        dfs(root)
        return LCA