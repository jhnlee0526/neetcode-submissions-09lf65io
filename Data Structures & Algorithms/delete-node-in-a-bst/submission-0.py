# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # dfs recursively
        # Time: O(h), where h is the height of the tree
        #           - Each recursive call moves down one level
        #           - In balanced trees, h = log(n); in worst-case (skewed), h = n
        # Space: O(h), due to recursion stack
        #           - No extra data structures used
        
        # Base case: empty tree
        if not root:
            return None

        # Traverse left or right depending on key
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:   # key == root.val -> Found the node to delete
            if not root.left:           # Case 1: No left child
                return root.right

            elif not root.right:        # Case 2: No right child
                return root.left
                                        # Case 3: Two children
            replacement = root.right    #   Find 'in-order' successor (smallest in right subtree)
            while replacement.left:
                replacement = replacement.left

            root.val = replacement.val                                  # Replace current node's value with successor's value
            root.right = self.deleteNode(root.right, replacement.val)   # Delete the successor node (which now has a duplicate value)

        return root


            
            
        
