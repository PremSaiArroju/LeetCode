"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                # Connect left to right
                node.left.next = node.right

                # Connect right to next node's left (if available)
                if node.next:
                    node.right.next = node.next.left

                # Push right before left to ensure left is processed first
                stack.append(node.right)
                stack.append(node.left)

        return root      