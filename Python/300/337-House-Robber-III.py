import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]
            left_pair = dfs(root.left)
            right_pair = dfs(root.right)

            with_root = root.val + left_pair[1] + right_pair[1]
            without_root = max(left_pair) + max(right_pair)

            return [with_root, without_root]

        return max(dfs(root))

    def rob_v2(self, root: Optional[TreeNode]) -> int:
        cache = {None: 0}

        def dfs(root):
            if root in cache:
                return cache[root]

            cache[root] = root.val
            if root.left:
                cache[root] += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                cache[root] += dfs(root.right.left) + dfs(root.right.right)

            cache[root] = max(cache[root], dfs(root.left) + dfs(root.right))
            return cache[root]

        return dfs(root)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.test_cases = [
            (
                "Example 1",
                TreeNode(
                    3,
                    TreeNode(2, None, TreeNode(3)),
                    TreeNode(3, None, TreeNode(1)),
                ),
                7,
            ),
            (
                "Example 2",
                TreeNode(
                    3,
                    TreeNode(4, TreeNode(1), TreeNode(3)),
                    TreeNode(5, None, TreeNode(1)),
                ),
                9,
            ),
            (
                "Single node",
                TreeNode(10),
                10,
            ),
            (
                "Empty tree",
                None,
                0,
            ),
            (
                "Left skewed",
                TreeNode(
                    4,
                    TreeNode(
                        1,
                        TreeNode(
                            2,
                            TreeNode(3),
                        ),
                    ),
                ),
                7,
            ),
            (
                "Right skewed",
                TreeNode(
                    2,
                    None,
                    TreeNode(
                        3,
                        None,
                        TreeNode(4),
                    ),
                ),
                6,
            ),
            (
                "Choose children over root",
                TreeNode(
                    2,
                    TreeNode(10),
                    TreeNode(20),
                ),
                30,
            ),
            (
                "Deep optimal split",
                TreeNode(
                    10,
                    TreeNode(
                        1,
                        TreeNode(10),
                        TreeNode(1),
                    ),
                    TreeNode(
                        1,
                        None,
                        TreeNode(10),
                    ),
                ),
                31,
            ),
        ]

    def test_rob(self):
        for name, tree, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.rob(tree),
                    expected,
                )

    def test_rob_v2(self):
        for name, tree, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.rob_v2(tree),
                    expected,
                )
