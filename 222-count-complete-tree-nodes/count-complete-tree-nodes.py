# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_node = root
        left_height = 0
        while left_node:
            left_height += 1
            left_node = left_node.left

        right_node = root
        right_height = 0
        while right_node:
            right_height += 1
            right_node = right_node.right

        if left_height == right_height:
            return (1 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)