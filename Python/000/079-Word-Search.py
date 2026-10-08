from typing import List
import unittest


#################### Solution ####################
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path or board[r][c] != word[i]:
                return False

            path.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    def exist_v2(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                    word[i] != board[r][c] or visited[r][c]):
                return False

            visited[r][c] = True
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.implementations = [
            self.solution.exist,
            self.solution.exist_v2,
        ]

    def test_exist(self):
        test_cases = [
            # Basic cases
            (
                [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]],
                "ABCCED",
                True,
            ),
            (
                [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]],
                "SEE",
                True,
            ),
            (
                [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]],
                "ABCB",
                False,
            ),

            # Single cell
            ([["A"]], "A", True),
            ([["A"]], "B", False),

            # Cannot reuse the same cell
            ([["A", "A"]], "AAA", False),

            # Word longer than the number of cells
            ([["A", "B"]], "ABC", False),

            # Single row
            ([["A", "B", "C"]], "ABC", True),

            # Single column
            ([["A"], ["B"], ["C"]], "ABC", True),

            # No matching path
            ([["A", "B"], ["C", "D"]], "ABDC", True),
            ([["A", "B"], ["C", "D"]], "ABCD", False),
        ]

        for func in self.implementations:
            for board, word, expected in test_cases:
                with self.subTest(
                        function=func.__name__,
                        board=board,
                        word=word,
                ):
                    self.assertEqual(func(board, word), expected)


if __name__ == "__main__":
    unittest.main()
