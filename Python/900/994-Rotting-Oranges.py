from collections import deque
from typing import List
import unittest


#################### Solution ####################
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(m * n)
        Space complexity: O(m * n)
        """
        q = deque()
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


###################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_orangesRotting(self):
        self.assertEqual(Solution().orangesRotting([
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]), 4)
        self.assertEqual(Solution().orangesRotting([
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ]), -1)
        self.assertEqual(Solution().orangesRotting([
            [0, 2]
        ]), 0)
