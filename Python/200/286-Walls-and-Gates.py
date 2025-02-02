from collections import deque
from typing import List
import unittest


class Solution:
    def islands_and_treasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        dist = 0

        def add_cell(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] == -1:
                return
            q.append([r, c])
            visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            dist += 1


###################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_islandsAndTreasure(self):
        grid = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647]
        ]
        solution = Solution()
        solution.islands_and_treasure(grid)
        self.assertEqual(grid, [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4]
        ])
