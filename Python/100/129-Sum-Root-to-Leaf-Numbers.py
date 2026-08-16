import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_numbers(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node, cur_val):
            cur_val.append(str(node.val))

            if not node.left and not node.right:
                values.append(int("".join(cur_val)))
            else:
                if node.left:
                    dfs(node.left, cur_val)

                if node.right:
                    dfs(node.right, cur_val)

            # backtracking
            cur_val.pop()

        if not root:
            return 0

        dfs(root, [])

        return sum(values)

    def sum_numbers_v2(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_num):
            if not node:
                return 0

            cur_num = cur_num * 10 + node.val

            if not node.left and not node.right:
                return cur_num

            return (
                    dfs(node.left, cur_num)
                    + dfs(node.right, cur_num)
            )

        return dfs(root, 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.sum_numbers,
            self.solution.sum_numbers_v2,
        ]

    def test_sum_numbers(self):
        test_cases = [
            {
                "name": "empty tree",
                "build_tree": lambda: None,
                "expected": 0,
            },
            {
                "name": "single node",
                "build_tree": lambda: TreeNode(5),
                "expected": 5,
            },
            {
                "name": "two root-to-leaf paths",
                "build_tree": lambda: TreeNode(
                    1,
                    left=TreeNode(2),
                    right=TreeNode(3),
                ),
                "expected": 25,  # 12 + 13
            },
            {
                "name": "different depth paths",
                "build_tree": lambda: TreeNode(
                    4,
                    left=TreeNode(
                        9,
                        left=TreeNode(5),
                        right=TreeNode(1),
                    ),
                    right=TreeNode(0),
                ),
                "expected": 1026,  # 495 + 491 + 40
            },
            {
                "name": "left skewed tree",
                "build_tree": lambda: TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        left=TreeNode(3),
                    ),
                ),
                "expected": 123,
            },
            {
                "name": "right skewed tree",
                "build_tree": lambda: TreeNode(
                    1,
                    right=TreeNode(
                        2,
                        right=TreeNode(3),
                    ),
                ),
                "expected": 123,
            },
            {
                "name": "tree containing zeros",
                "build_tree": lambda: TreeNode(
                    1,
                    left=TreeNode(
                        0,
                        left=TreeNode(0),
                    ),
                    right=TreeNode(5),
                ),
                "expected": 115,  # 100 + 15
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=case["name"],
                        expected=case["expected"],
                ):
                    root = case["build_tree"]()

                    actual = method(root)

                    self.assertEqual(actual, case["expected"])


if __name__ == "__main__":
    unittest.main()
