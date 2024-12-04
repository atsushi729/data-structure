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

    def diameter_of_binary_tree_v2(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res


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

    def test_diameter_of_binary_tree_v2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        solution = Solution()
        result = solution.diameter_of_binary_tree_v2(root)

        self.assertEqual(result, 3)
