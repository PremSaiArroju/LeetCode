# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        level_sums = []
        level_counts = []

        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()

            if level == len(level_sums):
                level_sums.append(node.val)
                level_counts.append(1)
            else:
                level_sums[level] += node.val
                level_counts[level] += 1

            # Stack: right first, then left so left gets processed first (like DFS)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

        return [level_sums[i] / level_counts[i] for i in range(len(level_sums))]