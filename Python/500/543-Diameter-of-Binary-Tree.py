# Definition for a binary tree node.
"""
        1
      /  \
     2    3
    / \
   4   5
"""

from typing import Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            res = max(res, left + right)

            return max(left, right) + 1

        dfs(root)

        return res


#################### Test Case ####################
class TestDiameterOfBinaryTree(unittest.TestCase):
    def test_diameter_of_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        solution = Solution()
        result = solution.diameter_of_binary_tree(root)

        self.assertEqual(result, 3)
