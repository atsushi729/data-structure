import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(
            self,
            root: Optional[TreeNode],
    ) -> int:
        node_val_list = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node_val_list.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        node_val_list.sort()
        min_diff = float("inf")

        for i in range(len(node_val_list) - 1):
            min_diff = min(
                min_diff,
                abs(node_val_list[i] - node_val_list[i + 1]),
            )

        return min_diff


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.methods = [
            self.sol.get_minimum_difference,
        ]

    def test_get_minimum_difference(self):
        test_cases = [
            {
                "name": "LeetCode example",
                "root": TreeNode(
                    4,
                    left=TreeNode(
                        2,
                        left=TreeNode(1),
                        right=TreeNode(3),
                    ),
                    right=TreeNode(6),
                ),
                "expected": 1,
            },
            {
                "name": "two nodes",
                "root": TreeNode(
                    1,
                    right=TreeNode(10),
                ),
                "expected": 9,
            },
            {
                "name": "minimum difference near root",
                "root": TreeNode(
                    10,
                    left=TreeNode(9),
                    right=TreeNode(20),
                ),
                "expected": 1,
            },
            {
                "name": "minimum difference in left subtree",
                "root": TreeNode(
                    10,
                    left=TreeNode(
                        5,
                        left=TreeNode(1),
                        right=TreeNode(6),
                    ),
                    right=TreeNode(20),
                ),
                "expected": 1,
            },
            {
                "name": "minimum difference in right subtree",
                "root": TreeNode(
                    10,
                    left=TreeNode(2),
                    right=TreeNode(
                        20,
                        left=TreeNode(15),
                        right=TreeNode(21),
                    ),
                ),
                "expected": 1,
            },
            {
                "name": "left skewed tree",
                "root": TreeNode(
                    10,
                    left=TreeNode(
                        7,
                        left=TreeNode(
                            3,
                            left=TreeNode(1),
                        ),
                    ),
                ),
                "expected": 2,
            },
            {
                "name": "right skewed tree",
                "root": TreeNode(
                    1,
                    right=TreeNode(
                        5,
                        right=TreeNode(
                            8,
                            right=TreeNode(20),
                        ),
                    ),
                ),
                "expected": 3,
            },
            {
                "name": "large values",
                "root": TreeNode(
                    100000,
                    left=TreeNode(1),
                    right=TreeNode(200001),
                ),
                "expected": 99999,
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=case["name"],
                ):
                    actual = method(case["root"])

                    self.assertEqual(
                        actual,
                        case["expected"],
                    )


if __name__ == "__main__":
    unittest.main()
