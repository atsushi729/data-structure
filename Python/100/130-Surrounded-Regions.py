from typing import List
import unittest
from collections import deque


#################### Solution ####################
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r - 1, c)
            capture(r + 1, c)
            capture(r, c - 1)
            capture(r, c + 1)

        for r in range(rows):
            if board[r][0] == "O":
                capture(r, 0, )
            if board[r][cols - 1] == "O":
                capture(r, cols - 1, )

        for c in range(cols):
            if board[0][c] == "O":
                capture(0, c)
            if board[rows - 1][c] == "O":
                capture(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

    def solve_v2(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def capture():
            q = deque()

            for r in range(rows):
                for c in range(cols):
                    if (r == 0 or r == rows - 1 or
                            c == 0 or c == cols - 1 and
                            board[r][c] == "O"):
                        q.append((r, c))

            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            q.append((nr, nc))

        capture()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_solve(self):
        solution = Solution()
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        solution.solve(board)
        self.assertListEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"]
            ]
        )
        board = [
            ["X"]
        ]
        solution.solve(board)
        self.assertListEqual(
            board,
            [
                ["X"]
            ]
        )
        board = [
            ["O"]
        ]
        solution.solve(board)
        self.assertListEqual(
            board,
            [
                ["O"]
            ]
        )
        board = [
            ["X", "O", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        solution.solve(board)
        self.assertListEqual(
            board,
            [
                ["X", "O", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]
            ]
        )

    def test_solve_v2(self):
        solution = Solution()
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        solution.solve_v2(board)
        self.assertListEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"]
            ]
        )
        board = [
            ["X"]
        ]
        solution.solve_v2(board)
        self.assertListEqual(
            board,
            [
                ["X"]
            ]
        )
        board = [
            ["O"]
        ]
        solution.solve_v2(board)
        self.assertListEqual(
            board,
            [
                ["O"]
            ]
        )
        board = [
            ["X", "O", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        solution.solve_v2(board)
        self.assertListEqual(
            board,
            [
                ["X", "O", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]
            ]
        )
