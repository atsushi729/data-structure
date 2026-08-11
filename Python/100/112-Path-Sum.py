import unittest
from typing import Optional


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(
            self,
            root: Optional[TreeNode],
            targetSum: int,
    ) -> bool:
        if not root:
            return False

        def dfs(node, cur_sum):
            cur_sum += node.val

            # leaf node
            if not node.left and not node.right:
                return cur_sum == targetSum

            if node.left and dfs(node.left, cur_sum):
                return True

            if node.right and dfs(node.right, cur_sum):
                return True

            return False

        return dfs(root, 0)


#################### Test ####################
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.has_path_sum,
        ]

    def test_has_path_sum(self):
        test_cases = [
            {
                "name": "empty tree",
                "root": None,
                "target_sum": 0,
                "expected": False,
            },
            {
                "name": "single node - match",
                "root": TreeNode(5),
                "target_sum": 5,
                "expected": True,
            },
            {
                "name": "single node - no match",
                "root": TreeNode(5),
                "target_sum": 1,
                "expected": False,
            },
            {
                "name": "valid root-to-leaf path",
                "root": TreeNode(
                    5,
                    left=TreeNode(
                        4,
                        left=TreeNode(
                            11,
                            left=TreeNode(7),
                            right=TreeNode(2),
                        ),
                    ),
                    right=TreeNode(
                        8,
                        left=TreeNode(13),
                        right=TreeNode(
                            4,
                            right=TreeNode(1),
                        ),
                    ),
                ),
                "target_sum": 22,
                "expected": True,
            },
            {
                "name": "no valid root-to-leaf path",
                "root": TreeNode(
                    1,
                    left=TreeNode(2),
                    right=TreeNode(3),
                ),
                "target_sum": 5,
                "expected": False,
            },
            {
                "name": "non-leaf partial path must not match",
                "root": TreeNode(
                    1,
                    left=TreeNode(2),
                ),
                "target_sum": 1,
                "expected": False,
            },
            {
                "name": "negative values",
                "root": TreeNode(
                    -2,
                    right=TreeNode(-3),
                ),
                "target_sum": -5,
                "expected": True,
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=case["name"],
                        target_sum=case["target_sum"],
                        expected=case["expected"],
                ):
                    actual = method(
                        case["root"],
                        case["target_sum"],
                    )

                    self.assertEqual(
                        actual,
                        case["expected"],
                    )
