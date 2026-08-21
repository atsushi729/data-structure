import unittest
from collections import deque
from typing import Optional


class Node:
    def __init__(
            self,
            val: int = 0,
            left: 'Node' = None,
            right: 'Node' = None,
            next: 'Node' = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(
            self,
            root: Optional[Node],
    ) -> Optional[Node]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for _ in range(level_size):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.methods = [
            self.sol.connect,
        ]

    def assert_next_equal(
            self,
            root: Optional[Node],
            expected: list[list[int]],
    ):
        if root is None:
            self.assertEqual(expected, [])
            return

        level_start = root
        actual = []

        while level_start:
            current = level_start
            level = []

            while current:
                level.append(current.val)
                current = current.next

            actual.append(level)

            next_level_start = None
            current = level_start

            while current and next_level_start is None:
                if current.left:
                    next_level_start = current.left
                elif current.right:
                    next_level_start = current.right

                current = current.next

            level_start = next_level_start

        self.assertEqual(actual, expected)

    def test_case(self):
        test_cases = [
            {
                "name": "empty tree",
                "root": None,
                "expected": [],
            },
            {
                "name": "single node",
                "root": Node(1),
                "expected": [
                    [1],
                ],
            },
            {
                "name": "perfect binary tree",
                "root": Node(
                    1,
                    left=Node(
                        2,
                        left=Node(4),
                        right=Node(5),
                    ),
                    right=Node(
                        3,
                        left=Node(6),
                        right=Node(7),
                    ),
                ),
                "expected": [
                    [1],
                    [2, 3],
                    [4, 5, 6, 7],
                ],
            },
            {
                "name": "left skewed tree",
                "root": Node(
                    1,
                    left=Node(
                        2,
                        left=Node(3),
                    ),
                ),
                "expected": [
                    [1],
                    [2],
                    [3],
                ],
            },
            {
                "name": "right skewed tree",
                "root": Node(
                    1,
                    right=Node(
                        2,
                        right=Node(3),
                    ),
                ),
                "expected": [
                    [1],
                    [2],
                    [3],
                ],
            },
            {
                "name": "non perfect binary tree",
                "root": Node(
                    1,
                    left=Node(
                        2,
                        left=Node(4),
                    ),
                    right=Node(
                        3,
                        right=Node(5),
                    ),
                ),
                "expected": [
                    [1],
                    [2, 3],
                    [4, 5],
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

                    self.assert_next_equal(
                        actual,
                        case["expected"],
                    )


if __name__ == "__main__":
    unittest.main()
