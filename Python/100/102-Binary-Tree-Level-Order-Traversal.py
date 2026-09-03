# Definition for a binary tree node.
import collections
import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
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

    def level_order_v2(self, root: Optional[TreeNode]) -> list[list[int]]:
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

    def level_order_v3(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_nodes = []
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_nodes:
                result.append(level_nodes)

        return result


class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.level_order,
            self.solution.level_order_v2,
            self.solution.level_order_v3,
        ]

    def test_level_order(self):
        test_cases = [
            {
                "name": "empty tree",
                "root": None,
                "expected": [],
            },
            {
                "name": "single node",
                "root": TreeNode(1),
                "expected": [[1]],
            },
            {
                "name": "LeetCode example",
                "root": TreeNode(
                    3,
                    left=TreeNode(9),
                    right=TreeNode(
                        20,
                        left=TreeNode(15),
                        right=TreeNode(7),
                    ),
                ),
                "expected": [
                    [3],
                    [9, 20],
                    [15, 7],
                ],
            },
            {
                "name": "complete binary tree",
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
                "expected": [
                    [1],
                    [2, 3],
                    [4, 5, 6, 7],
                ],
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
                "expected": [
                    [1],
                    [2],
                    [3],
                ],
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
                "expected": [
                    [1],
                    [2],
                    [3],
                ],
            },
            {
                "name": "sparse tree",
                "root": TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        right=TreeNode(4),
                    ),
                    right=TreeNode(
                        3,
                        left=TreeNode(5),
                    ),
                ),
                "expected": [
                    [1],
                    [2, 3],
                    [4, 5],
                ],
            },
            {
                "name": "negative values",
                "root": TreeNode(
                    -1,
                    left=TreeNode(-2),
                    right=TreeNode(
                        3,
                        left=TreeNode(-4),
                        right=TreeNode(5),
                    ),
                ),
                "expected": [
                    [-1],
                    [-2, 3],
                    [-4, 5],
                ],
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=case["name"],
                ):
                    actual = method(case["root"])

                    self.assertListEqual(
                        actual,
                        case["expected"],
                    )


if __name__ == "__main__":
    unittest.main()
