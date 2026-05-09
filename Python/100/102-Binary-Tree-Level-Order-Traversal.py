# Definition for a binary tree node.
import collections
import unittest
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            current_level = []

            for _ in range(queue_len):
                node = queue.popleft()

                if node:
                    current_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if current_level:
                level.append(current_level)

        return level

    def level_order_v2(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res


class TestLevelOrder(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

        self.test_cases = [
            (
                "Empty Tree",
                None,
                []
            ),
            (
                "Single Node",
                TreeNode(1),
                [[1]]
            ),
            (
                "Complete Binary Tree",
                TreeNode(
                    3,
                    TreeNode(9),
                    TreeNode(20, TreeNode(15), TreeNode(7))
                ),
                [[3], [9, 20], [15, 7]]
            ),
            (
                "Right Skewed Tree",
                TreeNode(
                    1,
                    None,
                    TreeNode(
                        2,
                        None,
                        TreeNode(3)
                    )
                ),
                [[1], [2], [3]]
            ),
            (
                "Left Skewed Tree",
                TreeNode(
                    1,
                    TreeNode(
                        2,
                        TreeNode(3)
                    )
                ),
                [[1], [2], [3]]
            ),
            (
                "Sparse Tree",
                TreeNode(
                    1,
                    TreeNode(2, None, TreeNode(4)),
                    TreeNode(3, TreeNode(5), None)
                ),
                [[1], [2, 3], [4, 5]]
            ),
            (
                "Negative Values",
                TreeNode(
                    -1,
                    TreeNode(-2),
                    TreeNode(3, TreeNode(-4), TreeNode(5))
                ),
                [[-1], [-2, 3], [-4, 5]]
            ),
        ]

    def test_level_order(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.level_order(root),
                    expected
                )

    def test_level_order_v2(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.level_order_v2(root),
                    expected
                )
