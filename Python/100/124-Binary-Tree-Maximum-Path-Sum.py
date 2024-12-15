import unittest
from typing import Optional


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            res = max(res, left + right + node.val)
            return max(left, right) + node.val

        dfs(root)
        return res

    def max_path_sum_v2(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = self.get_max(node.left)
            right = self.get_max(node.right)
            res = max(res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res

    def get_max(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.get_max(root.left)
        right = self.get_max(root.right)
        path = root.val + max(left, right)
        return max(0, path)


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_max_path_sum(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(Solution().max_path_sum(root), 6)
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().max_path_sum(root), 42)

    def test_max_path_sum_v2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(Solution().max_path_sum_v2(root), 6)
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().max_path_sum_v2(root), 42)
