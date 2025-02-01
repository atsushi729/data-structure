from typing import List
import unittest


#################### Solution ####################
class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(m * n)
        Space complexity: O(m * n)
        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        result = []

        def dfs(r, c, ocean, prev_height):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in ocean or heights[r][c] < prev_height:
                return
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result


###################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_pacificAtlantic(self):
        self.assertEqual(Solution().pacific_atlantic([
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]), [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
