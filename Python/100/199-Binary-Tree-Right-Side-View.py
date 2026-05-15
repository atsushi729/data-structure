import collections
import unittest
from typing import Optional, List
from collections import deque


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = collections.deque([root])

        while queue:
            q_len = len(queue)
            right_node = None

            for _ in range(q_len):
                node = queue.popleft()

                if node:
                    right_node = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right_node:
                result.append(right_node.val)

        return result

    def right_side_view_2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def right_side_view_3(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == level_size - 1:
                    result.append(node.val)

        return result


#################### Test Case ####################
class TestRightSideView(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.test_cases = [
            ("Empty Tree", None, []),
            (
                "Single Node",
                TreeNode(1),
                [1],
            ),
            (
                "Example 1",
                TreeNode(
                    1,
                    TreeNode(2, None, TreeNode(5)),
                    TreeNode(3, None, TreeNode(4)),
                ),
                [1, 3, 4],
            ),
            (
                "Left Skewed Tree",
                TreeNode(
                    1,
                    TreeNode(
                        2,
                        TreeNode(3),
                    ),
                ),
                [1, 2, 3],
            ),
            (
                "Right Skewed Tree",
                TreeNode(
                    1,
                    None,
                    TreeNode(
                        2,
                        None,
                        TreeNode(3),
                    ),
                ),
                [1, 2, 3],
            ),
        ]

    def test_right_side_view(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(self.solution.right_side_view(root), expected)

    def test_right_side_view_2(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(self.solution.right_side_view_2(root), expected)

    def test_right_side_view_3(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(self.solution.right_side_view_3(root), expected)


if __name__ == "__main__":
    unittest.main()
