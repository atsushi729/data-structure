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

        # Helper nodes
        leaf_1 = Node(1, True)
        leaf_0 = Node(0, True)

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
                "All same values",
                [
                    [1, 1],
                    [1, 1],
                ],
                Node(1, True),
            ),
            (
                "Split into four leaves",
                [
                    [1, 0],
                    [0, 1],
                ],
                Node(
                    0,
                    False,
                    Node(1, True),
                    Node(0, True),
                    Node(0, True),
                    Node(1, True),
                ),
            ),
            (
                "LeetCode example",
                [
                    [1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                ],
                Node(
                    0,
                    False,
                    leaf_1,
                    leaf_0,
                    leaf_0,
                    leaf_1,
                ),
            ),
        ]

    def is_same_tree(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False

        if node1.isLeaf != node2.isLeaf:
            return False

        return (
                self.is_same_tree(node1.topLeft, node2.topLeft)
                and self.is_same_tree(node1.topRight, node2.topRight)
                and self.is_same_tree(node1.bottomLeft, node2.bottomLeft)
                and self.is_same_tree(node1.bottomRight, node2.bottomRight)
        )

    def test_construct(self):
        for name, grid, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.solution.construct(grid)

                self.assertTrue(
                    self.is_same_tree(result, expected)
                )

    def test_construct_v2(self):
        for name, grid, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.solution.construct_v2(grid)
                self.assertTrue(
                    self.is_same_tree(result, expected)
                )

    def test_construct_v3(self):
        for name, grid, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.solution.construct_v3(grid)
                self.assertTrue(
                    self.is_same_tree(result, expected)
                )


if __name__ == "__main__":
    unittest.main()
