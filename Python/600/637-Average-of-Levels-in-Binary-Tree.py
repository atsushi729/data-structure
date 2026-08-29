import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def average_of_levels(
            self,
            root: Optional[TreeNode],
    ) -> list[float]:
        if not root:
            return []

        queue = deque([root])
        level_average = []

        while queue:
            current_val = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                current_val += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_average.append(
                float(current_val / level_size),
            )

        return level_average


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.methods = [
            self.sol.average_of_levels,
        ]

    def assert_float_lists_equal(
            self,
            actual: list[float],
            expected: list[float],
    ):
        # Verify that both lists contain the same number of values.
        self.assertEqual(len(actual), len(expected))

        # Compare floating-point values with tolerance.
        for actual_value, expected_value in zip(actual, expected):
            self.assertAlmostEqual(
                actual_value,
                expected_value,
                places=7,
            )

    def test_average_of_levels(self):
        test_cases = [
            {
                "name": "empty tree",
                "root": None,
                "expected": [],
            },
            {
                "name": "single node",
                "root": TreeNode(1),
                "expected": [1.0],
            },
            {
                "name": "LeetCode example",
                "root": TreeNode(
                    3,
                    left=TreeNode(
                        9,
                    ),
                    right=TreeNode(
                        20,
                        left=TreeNode(15),
                        right=TreeNode(7),
                    ),
                ),
                "expected": [3.0, 14.5, 11.0],
            },
            {
                "name": "balanced tree",
                "root": TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        left=TreeNode(4),
                        right=TreeNode(5),
                    ),
                    right=TreeNode(
                        3,
                        left=TreeNode(6),
                        right=TreeNode(7),
                    ),
                ),
                "expected": [1.0, 2.5, 5.5],
            },
            {
                "name": "left skewed tree",
                "root": TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        left=TreeNode(3),
                    ),
                ),
                "expected": [1.0, 2.0, 3.0],
            },
            {
                "name": "right skewed tree",
                "root": TreeNode(
                    1,
                    right=TreeNode(
                        2,
                        right=TreeNode(3),
                    ),
                ),
                "expected": [1.0, 2.0, 3.0],
            },
            {
                "name": "negative values",
                "root": TreeNode(
                    -1,
                    left=TreeNode(-2),
                    right=TreeNode(-4),
                ),
                "expected": [-1.0, -3.0],
            },
            {
                "name": "uneven tree",
                "root": TreeNode(
                    10,
                    left=TreeNode(
                        5,
                        left=TreeNode(2),
                    ),
                    right=TreeNode(15),
                ),
                "expected": [10.0, 10.0, 2.0],
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=case["name"],
                ):
                    actual = method(case["root"])

                    self.assert_float_lists_equal(
                        actual,
                        case["expected"],
                    )


if __name__ == "__main__":
    unittest.main()