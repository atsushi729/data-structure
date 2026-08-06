import unittest
from typing import Optional


class TreeNode:
    def __init__(
            self,
            val=0,
            left=None,
            right=None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(
            self,
            root: Optional[TreeNode],
    ) -> bool:
        if not root:
            return True

        def dfs(
                left: Optional[TreeNode],
                right: Optional[TreeNode],
        ) -> bool:
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (
                    left.val == right.val
                    and dfs(left.left, right.right)
                    and dfs(left.right, right.left)
            )

        return dfs(root.left, root.right)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    @staticmethod
    def build_tree(
            values: list[Optional[int]],
    ) -> Optional[TreeNode]:
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = [root]
        index = 1

        while queue and index < len(values):
            node = queue.pop(0)

            if index < len(values) and values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)

            index += 1

            if index < len(values) and values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)

            index += 1

        return root

    def get_test_cases(self):
        return [
            # Empty tree
            ([], True),

            # Single-node tree
            ([1], True),

            # Symmetric tree
            ([1, 2, 2, 3, 4, 4, 3], True),

            # Symmetric tree with missing nodes
            ([1, 2, 2, None, 3, 3, None], True),

            # Asymmetric structure
            ([1, 2, 2, None, 3, None, 3], False),

            # Different values at the same mirrored position
            ([1, 2, 2, 3, 4, 4, 5], False),

            # Only the left child exists
            ([1, 2], False),

            # Only the right child exists
            ([1, None, 2], False),

            # Two equal child nodes
            ([1, 2, 2], True),

            # Two different child nodes
            ([1, 2, 3], False),

            # Deeper symmetric tree
            (
                [
                    1,
                    2, 2,
                    3, 4, 4, 3,
                    5, None, None, 6, 6, None, None, 5,
                ],
                True,
            ),

            # Deeper asymmetric tree
            (
                [
                    1,
                    2, 2,
                    3, 4, 4, 3,
                    5, None, None, 6, 7, None, None, 5,
                ],
                False,
            ),

            # Negative values in a symmetric tree
            ([-1, -2, -2, -3, -4, -4, -3], True),

            # Duplicate values with asymmetric structure
            ([1, 1, 1, 1, None, 1, None], False),
        ]

    def test_is_symmetric(self):
        methods = [
            self.solution.is_symmetric,
        ]

        for method in methods:
            for values, expected in self.get_test_cases():
                with self.subTest(
                        method=method.__name__,
                        values=values,
                        expected=expected,
                ):
                    # Build a new tree for every test execution
                    root = self.build_tree(values)

                    result = method(root)

                    self.assertEqual(
                        result,
                        expected,
                    )


if __name__ == "__main__":
    unittest.main()
