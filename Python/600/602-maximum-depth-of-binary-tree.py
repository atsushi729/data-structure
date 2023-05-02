# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def __init__(self):
        self.counter = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root.val:
            self.counter += 1

        self.maxDepth(root.left)
        self.maxDepth(root.right)

        return counter
        # depth = math.log2(len(root))
        # return depth