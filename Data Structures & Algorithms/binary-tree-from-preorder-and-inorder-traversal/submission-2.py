# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # DFS rercursively
        #   Time : O(n^2) — due to slicing and index lookup in each recursive call
        #   Space: O(n) — recursion stack + cumulative cost of list slicing

        def dfs(preorder, inorder):
            # base case
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            rIdx = inorder.index(preorder[0])   # O(n) time

            root.left = dfs(preorder[1 : rIdx + 1], inorder[: rIdx])
            root.right = dfs(preorder[rIdx + 1 :], inorder[rIdx + 1 :])

            return root
        
        return dfs(preorder, inorder)

        
        