# Definition for a binary tree node.
from collections import deque
from typing import Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    def max_depth_v2(self, root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return 0

        return 1 + max(self.max_depth_v2(root.left), self.max_depth_v2(root.right))


#################### Test Case ####################
class TestMaxDepth(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.solution = Solution()
        cls.tests = [
            ("Balanced Tree", TreeNode(1, TreeNode(2), TreeNode(3)), 2),
            ("Left Tree", TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(3)), 3),
            ("Right Tree", TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))), 3),
        ]

    def test_max_depth(self):
        for name, tree, expected in self.tests:
            with self.subTest(name=name):
                self.assertEqual(self.solution.max_depth(tree), expected)

    def test_max_depth_v2(self):
        for name, tree, expected in self.tests:
            with self.subTest(name=name):
                self.assertEqual(self.solution.max_depth_v2(tree), expected)
