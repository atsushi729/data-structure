# Definition for a QuadTree node.
import unittest


class Node:
    def __init__(
            self,
            val,
            isLeaf,
            topLeft=None,
            topRight=None,
            bottomLeft=None,
            bottomRight=None
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        def dfs(n, r, c):
            all_same = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False
                        break

            if all_same:
                return Node(grid[r][c], True)

            n = n // 2

            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            return Node(
                0,
                False,
                top_left,
                top_right,
                bottom_left,
                bottom_right
            )

        return dfs(len(grid), 0, 0)

    def construct_v2(self, grid: list[list[int]]) -> 'Node':
        def build_tree(size, row, col):
            base_value = grid[row][col]
            is_uniform = True

            for i in range(size):
                for j in range(size):
                    if grid[row + i][col + j] != base_value:
                        is_uniform = False
                        break
            if is_uniform:
                return Node(base_value, True)

            half_size = size // 2
            top_left = build_tree(half_size, row, col)
            top_right = build_tree(half_size, row, col + half_size)
            bottom_left = build_tree(half_size, row + half_size, col)
            bottom_right = build_tree(half_size, row + half_size, col + half_size)

            return Node(
                0,
                False,
                top_left,
                top_right,
                bottom_left,
                bottom_right
            )

        return build_tree(len(grid), 0, 0)

    def construct_v3(self, grid: list[list[int]]) -> 'Node':
        leafNodes = {
            0: Node(False, True),
            1: Node(True, True)
        }

        def dfs(n, r, c):
            if n == 1:
                return leafNodes[grid[r][c]]

            n //= 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            if (topLeft.isLeaf and topRight.isLeaf and
                    bottomLeft.isLeaf and bottomRight.isLeaf and
                    topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return topLeft

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.methods = [
            cls.solution.construct,
            cls.solution.construct_v2,
            cls.solution.construct_v3,
        ]

        cls.test_cases = [
            (
                "Single cell - 1",
                [[1]],
                Node(1, True),
            ),
            (
                "Single cell - 0",
                [[0]],
                Node(0, True),
            ),
            (
                "All ones",
                [
                    [1, 1],
                    [1, 1],
                ],
                Node(1, True),
            ),
            (
                "All zeros",
                [
                    [0, 0],
                    [0, 0],
                ],
                Node(0, True),
            ),
            (
                "Four different quadrants",
                [
                    [1, 0],
                    [0, 1],
                ],
                Node(
                    0, False,
                    Node(1, True),
                    Node(0, True),
                    Node(0, True),
                    Node(1, True),
                ),
            ),
            (
                "4x4 uniform quadrants",
                [
                    [1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                ],
                Node(
                    0, False,
                    Node(1, True),
                    Node(0, True),
                    Node(0, True),
                    Node(1, True),
                ),
            ),
            (
                "4x4 mixed quadrant",
                [
                    [1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                ],
                Node(
                    0, False,
                    Node(1, True),
                    Node(0, True),
                    Node(0, True),
                    Node(
                        0, False,
                        Node(1, True),
                        Node(0, True),
                        Node(0, True),
                        Node(1, True),
                    ),
                ),
            ),
        ]

    def serialize(self, node):
        if node is None:
            return None

        if node.isLeaf:
            return (True, bool(node.val))

        return (
            False,
            self.serialize(node.topLeft),
            self.serialize(node.topRight),
            self.serialize(node.bottomLeft),
            self.serialize(node.bottomRight),
        )

    def test_construct(self):
        for method in self.methods:
            for name, grid, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=name,
                ):
                    result = method(grid)

                    self.assertEqual(
                        self.serialize(result),
                        self.serialize(expected),
                    )
