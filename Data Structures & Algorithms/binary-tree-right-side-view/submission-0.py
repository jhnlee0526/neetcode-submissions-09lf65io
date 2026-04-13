# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs recursively: bottom-up
        #   Time : O(N)
        #           - Each node is visited once.
        #           - Sorting levels is O(D log D), where D is the number of distinct depths, but D ≤ N.
        #   Space: O(N)
        #           - levels dict stores up to N nodes.
        #           - Call stack depth is O(H), where H is the height of the tree.

        levels = {} # {depth1: [node1, node2, node3], ...}

        def dfs(node, depth): # recursively, bottom-up
            if not node:
                return
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

            if depth not in levels:
                levels[depth] = []
            levels[depth].append(node.val)

        dfs(root, 0)    # start at depth 0

        # return [nodes[-1] for depth, nodes in sorted(levels.items())]
        return [levels[depth][-1] for depth in sorted(levels.keys())]   # sorted(levels)



        
