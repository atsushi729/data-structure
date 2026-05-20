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
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):

            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))

    def is_valid_bst2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()

            if not (left < node.val < right):
                return False

            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True

    def is_valid_bst3(self, root: Optional[TreeNode]) -> bool:
        def validate_bst(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False

            return (
                    validate_bst(node.left, lower, node.val)
                    and validate_bst(node.right, node.val, upper)
            )

        return validate_bst(root, float("-inf"), float("inf"))


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.test_cases = [
            (
                "Valid BST",
                TreeNode(2, TreeNode(1), TreeNode(3)),
                True,
            ),
            (
                "Invalid right subtree",
                TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))),
                False,
            ),
            (
                "Invalid lower bound in right subtree",
                TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7))),
                False,
            ),
            (
                "Single node",
                TreeNode(1),
                True,
            ),
            (
                "Empty tree",
                None,
                True,
            ),
            (
                "Duplicate value on left",
                TreeNode(2, TreeNode(2), TreeNode(3)),
                False,
            ),
            (
                "Duplicate value on right",
                TreeNode(2, TreeNode(1), TreeNode(2)),
                False,
            ),
            (
                "Valid negative values",
                TreeNode(0, TreeNode(-3), TreeNode(9)),
                True,
            ),
        ]

    def test_is_valid_bst(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.is_valid_bst(root),
                    expected,
                )

    def test_is_valid_bst2(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.is_valid_bst2(root),
                    expected,
                )

    def test_is_valid_bst3(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.is_valid_bst3(root),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
