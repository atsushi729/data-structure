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
        max_sum = root.val

        def get_max_sum(node):
            nonlocal max_sum
            if not node:
                return 0
            # 左右の子ノードからの最大一方向パス和を計算（負になる場合は0を返す）
            left = max(get_max_sum(node.left), 0)
            right = max(get_max_sum(node.right), 0)

            # このノードを通るパスの最大値でmax_sumを更新
            max_sum = max(max_sum, node.val + left + right)

            # 親ノードに返すのは、一方向最大パス和
            return node.val + max(left, right)

        get_max_sum(root)
        return max_sum

    def max_path_sum_v3(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def dfs(root):
            nonlocal res
            if not root:
                return
            left = self.getMax(root.left)
            right = self.getMax(root.right)
            res = max(res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res

    def getMax(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.getMax(root.left)
        right = self.getMax(root.right)
        path = root.val + max(left, right)
        return max(0, path)


#################### Test ####################
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.max_path_sum,
            self.solution.max_path_sum_v2,
            self.solution.max_path_sum_v3,
        ]

    def test_max_path_sum(self):
        test_cases = [
            {
                "name": "simple tree",
                "build_tree": lambda: TreeNode(
                    1,
                    left=TreeNode(2),
                    right=TreeNode(3),
                ),
                "expected": 6,
            },
            {
                "name": "LeetCode example",
                "build_tree": lambda: TreeNode(
                    -10,
                    left=TreeNode(9),
                    right=TreeNode(
                        20,
                        left=TreeNode(15),
                        right=TreeNode(7),
                    ),
                ),
                "expected": 42,
            },
            {
                "name": "single node",
                "build_tree": lambda: TreeNode(5),
                "expected": 5,
            },
            {
                "name": "single negative node",
                "build_tree": lambda: TreeNode(-5),
                "expected": -5,
            },
            {
                "name": "all negative",
                "build_tree": lambda: TreeNode(
                    -3,
                    left=TreeNode(-2),
                    right=TreeNode(-5),
                ),
                "expected": -2,
            },
            {
                "name": "maximum path does not include root",
                "build_tree": lambda: TreeNode(
                    -10,
                    left=TreeNode(
                        5,
                        left=TreeNode(4),
                        right=TreeNode(6),
                    ),
                    right=TreeNode(-20),
                ),
                "expected": 15,  # 4 -> 5 -> 6
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
                "expected": 6,
            },
            {
                "name": "negative branch should be ignored",
                "build_tree": lambda: TreeNode(
                    10,
                    left=TreeNode(-5),
                    right=TreeNode(20),
                ),
                "expected": 30,
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
