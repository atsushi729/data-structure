from typing import List
import unittest


#################### Solution ####################
class Solution:
    def solve_n_queens(self, n: int) -> List[List[str]]:
        col = set()
        pos_dig = set()
        neg_dig = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in pos_dig or (r - c) in neg_dig:
                    continue

                col.add(c)
                pos_dig.add(r + c)
                neg_dig.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pos_dig.remove(r + c)
                neg_dig.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

    def solve_n_queens_v2(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if self.is_safe(r, c, board):
                    board[r][c] = 'Q'
                    backtrack(r + 1)
                    board[r][c] = "."

        backtrack(0)
        return res

    def is_safe(self, r: int, c: int, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_solve_n_queens(self):
        solution = Solution()
        self.assertListEqual(
            solution.solve_n_queens(4),
            [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."]
            ]
        )

    def test_solve_n_queens_v2(self):
        solution = Solution()
        self.assertListEqual(
            solution.solve_n_queens_v2(4),
            [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."]
            ]
        )
