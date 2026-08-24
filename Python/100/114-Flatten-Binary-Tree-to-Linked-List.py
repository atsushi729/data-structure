import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        val_list = []

        def dfs(node):
            if not node:
                return None

            val_list.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        current = root
        root.left = None

        for val in val_list[1:]:
            current.right = TreeNode(val)
            current = current.right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.methods = [
            self.sol.flatten,
        ]

    def assert_flattened_tree(
            self,
            root: Optional[TreeNode],
            expected_values: list[int],
    ):
        """
        Verify that the flattened tree satisfies these conditions:

        1. Nodes appear in preorder traversal order.
        2. Every left pointer is None.
        3. The number of nodes matches the expected values.
        """
        current = root

        for expected_value in expected_values:
            self.assertIsNotNone(current)
            self.assertEqual(current.val, expected_value)
            self.assertIsNone(current.left)

            current = current.right

        # Verify that there are no extra nodes.
        self.assertIsNone(current)

    def test_flatten(self):
        test_cases = [
            {
                "name": "empty tree",
                "root": None,
                "expected": [],
            },
            {
                "name": "single node",
                "root": TreeNode(1),
                "expected": [1],
            },
            {
                "name": "LeetCode example",
                "root": TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        left=TreeNode(3),
                        right=TreeNode(4),
                    ),
                    right=TreeNode(
                        5,
                        right=TreeNode(6),
                    ),
                ),
                "expected": [1, 2, 3, 4, 5, 6],
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
                "expected": [1, 2, 3],
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
                "expected": [1, 2, 3],
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
                "expected": [1, 2, 4, 5, 3, 6, 7],
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=case["name"],
                ):
                    method(case["root"])

                    self.assert_flattened_tree(
                        case["root"],
                        case["expected"],
                    )


if __name__ == "__main__":
    unittest.main()
