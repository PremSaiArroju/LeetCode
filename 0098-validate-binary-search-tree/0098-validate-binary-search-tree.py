# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, min_val, max_val):
            if not node:
                return True  # Empty node = always valid
            
            # If node breaks the BST rule
            if node.val <= min_val or node.val >= max_val:
                return False

            # Left child must be < current node
            # Right child must be > current node
            return check(node.left, min_val, node.val) and check(node.right, node.val, max_val)

        return check(root, float('-inf'), float('inf'))