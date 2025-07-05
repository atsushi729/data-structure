from typing import List
import heapq
import unittest


class Solution:
    def swim_in_water(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        min_h = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))

        while min_h:
            t, r, c = heapq.heappop(min_h)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                nei_r, nei_c = r + dr, c + dc
                if nei_r < 0 or nei_c < 0 or nei_r == n or nei_c == n or (nei_r, nei_c) in visit:
                    continue
                visit.add((nei_r, nei_c))
                heapq.heappush(min_h, [max(t, grid[nei_r][nei_c]), nei_r, nei_c])


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([[0, 2], [1, 3]], 3),
            ([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]], 16),
            ([[0]], 0),
            ([[0, 1], [2, 3]], 3),
            ([[0, 1], [4, 2]], 2)
        ]

    def test_swim_in_water(self):
        for grid, expected in self.test_cases:
            result = self.solution.swim_in_water(grid)
            self.assertEqual(result, expected, f"Failed for grid: {grid}, expected: {expected}, got: {result}")
