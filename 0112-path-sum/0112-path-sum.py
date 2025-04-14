# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Stack stores (node, current_sum)
        stack = [(root, root.val)]
        
        while stack:
            node, current_sum = stack.pop()

            # If it's a leaf and current sum == target
            if not node.left and not node.right and current_sum == targetSum:
                return True

            if node.right:
                stack.append((node.right, current_sum + node.right.val))
            if node.left:
                stack.append((node.left, current_sum + node.left.val))

        return False  