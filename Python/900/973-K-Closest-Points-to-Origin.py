import unittest
from typing import List
import heapq


#################### Solution ####################
class Solution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]

    def k_closest_v2(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            min_heap.append((distance, point))

        heapq.heapify(min_heap)

        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])
        return result


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_k_closest(self):
        solution = Solution()
        self.assertListEqual(solution.k_closest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertListEqual(solution.k_closest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])

    def test_k_closest_v2(self):
        solution = Solution()
        self.assertListEqual(solution.k_closest_v2([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertListEqual(solution.k_closest_v2([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
