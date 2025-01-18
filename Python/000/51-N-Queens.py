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
