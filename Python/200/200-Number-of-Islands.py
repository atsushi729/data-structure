from typing import List
import unittest


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
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
