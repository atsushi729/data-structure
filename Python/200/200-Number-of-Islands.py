from collections import deque
from typing import List
import unittest


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        """
        Time complexity (m * n)
        Space complexity (m * n)
        """
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Down, Up, Right, Left
        rows, cols = len(grid), len(grid[0])
        is_land = 0

        def dfs(r, c):
            # Check if the current cell is out of bound or it is water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    is_land += 1

        return is_land

    def num_islands_v2(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Down, Up, Right, Left
        rows, cols = len(grid), len(grid[0])
        is_land = 0

        def bfs(r, c):
            grid[r][c] = "0"
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Check if the current cell is out of bound or it is water
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    is_land += 1

        return is_land


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_num_islands(self):
        solution = Solution()
        self.assertEqual(solution.num_islands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]), 1)
        self.assertEqual(solution.num_islands([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]), 3)

    def test_num_islands_v2(self):
        solution = Solution()
        self.assertEqual(solution.num_islands_v2([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]), 1)
        self.assertEqual(solution.num_islands_v2([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]), 3)
