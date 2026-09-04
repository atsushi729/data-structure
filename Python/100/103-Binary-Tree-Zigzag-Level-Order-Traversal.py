import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        queue = deque([root] if root else [])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(res) % 2:
                level.reverse()
            res.append(level)

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.zigzag_level_order,
        ]

    def test_zigzag_level_order(self):
        test_cases = [
            {
                "name": "Base Case",
                "root": TreeNode(
                    3,
                    left=TreeNode(9),
                    right=TreeNode(
                        20,
                        left=TreeNode(15),
                        right=TreeNode(7)
                    ),
                ),
                "expected": [[3], [20, 9], [15, 7]]
            }
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(method=method, case=case["name"]):
                    actual = method(case["root"])
                    self.assertListEqual(actual, case["expected"])

