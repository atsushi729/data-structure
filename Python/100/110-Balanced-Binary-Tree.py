# Definition for a binary tree node.
import unittest
from typing import Optional


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # Base case
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

    def is_balanced_v2(self, root: Optional[TreeNode]) -> bool:
        """
        time complexity: O(n^2)
        space complexity: O(n)
        """
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            return False

        return self.is_balanced_v2(root.left) and self.is_balanced_v2(root.right)

    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def is_balanced_v3(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            if not node:
                return 0

            left = check_height(node.left)
            if left == -1:
                return -1

            right = check_height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check_height(root) != -1


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()
        cls.test_cases = [
            # (テスト名, ツリーのルート, 期待される結果)
            ("空の木", None, True),
            ("単一ノード", TreeNode(1), True),
            ("バランスの取れた木",
             TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))),
             True),
            ("バランスの取れていない木",
             TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
             False),
        ]

    def test_solution(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(self.sol.is_balanced(root), expected)

    def test_solution_v2(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(self.sol.is_balanced(root), expected)

    def test_solution_v3(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(self.sol.is_balanced(root), expected)


#################### Not Working ####################
# This solution only check from root node, so it cannot check from child node.
class NotSolution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def max_height(node):
            if not node:
                return 0

            left = max_height(node.left)
            right = max_height(node.right)
            return max(left, right) + 1

        left_height = max_height(root.left)
        right_height = max_height(root.right)
        diff = abs(left_height - right_height)

        if diff > 1:
            return False
        return True
