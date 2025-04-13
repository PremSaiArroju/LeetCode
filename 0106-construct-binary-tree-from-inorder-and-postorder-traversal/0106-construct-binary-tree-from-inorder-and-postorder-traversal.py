# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # Create a hashmap to store the indices of elements in the inorder list
        inorder_map = {val: index for index, val in enumerate(inorder)}

        # Define a recursive function to build the binary tree
        def build(post_start, post_end, in_start, in_end):
            # Base case: If the start index in the postorder list is greater than the end index,
            # it indicates that the current subtree is null, so return None
            if post_start > post_end:
                return None

            # Extract the value of the root node from the postorder list using the end index
            root_val = postorder[post_end]
            root = TreeNode(root_val)

            # Find the index of the root node's value in the inorder list using the hashmap
            in_index = inorder_map[root_val]

            # Determine the size of the left subtree
            left_size = in_index - in_start

            # Recursively build the left subtree
            root.left = build(
                post_start, post_start + left_size - 1, in_start, in_index - 1
            )

            # Recursively build the right subtree
            root.right = build(
                post_start + left_size, post_end - 1, in_index + 1, in_end
            )

            return root

        # Call the build function with initial parameters corresponding to the entire postorder and inorder lists
        return build(0, len(postorder) - 1, 0, len(inorder) - 1)
