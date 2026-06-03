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


#################### Test Case ####################
class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        # Case 1
        tree1 = TreeNode(
            1,
            TreeNode(2),
            TreeNode(3)
        )

        # Case 2
        tree2 = TreeNode(
            -10,
            TreeNode(9),
            TreeNode(
                20,
                TreeNode(15),
                TreeNode(7)
            )
        )

        # Case 3: single node
        tree3 = TreeNode(5)

        # Case 4: all negative
        tree4 = TreeNode(
            -3,
            TreeNode(-2),
            TreeNode(-5)
        )

        cls.test_cases = [
            ("Simple tree", tree1, 6),
            ("LeetCode example", tree2, 42),
            ("Single node", tree3, 5),
            ("All negative", tree4, -2),
        ]

    def test_max_path_sum(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.max_path_sum(root),
                    expected
                )

    def test_max_path_sum_v2(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.max_path_sum_v2(root),
                    expected
                )

    def test_max_path_sum_v3(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.max_path_sum_v3(root),
                    expected
                )
