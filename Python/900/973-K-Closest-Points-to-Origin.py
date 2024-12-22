import unittest
from typing import List


#################### Solution ####################
class Solution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_k_closest(self):
        solution = Solution()
        self.assertListEqual(solution.k_closest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertListEqual(solution.k_closest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
