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
    def setUp(self):
        self.sol = Solution()
        self.methods = [
            self.sol.k_closest,
            self.sol.k_closest_v2,
        ]

    def test_k_closest(self):
        test_cases = [
            {
                "name": "k equals 1",
                "points": [[1, 3], [-2, 2]],
                "k": 1,
                "expected": [[-2, 2]],
            },
            {
                "name": "k equals 2",
                "points": [[3, 3], [5, -1], [-2, 4]],
                "k": 2,
                "expected": [[3, 3], [-2, 4]],
            },
            {
                "name": "single point",
                "points": [[1, 1]],
                "k": 1,
                "expected": [[1, 1]],
            },
            {
                "name": "all points",
                "points": [[1, 0], [2, 0], [3, 0]],
                "k": 3,
                "expected": [[1, 0], [2, 0], [3, 0]],
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=case["name"],
                ):
                    points = [point[:] for point in case["points"]]

                    result = method(points, case["k"])

                    self.assertListEqual(
                        result,
                        case["expected"],
                    )


if __name__ == "__main__":
    unittest.main()
