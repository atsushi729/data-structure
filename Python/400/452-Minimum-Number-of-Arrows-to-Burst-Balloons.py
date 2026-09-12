import unittest


class Solution:
    def find_min_arrow_shots(self, points: list[list[int]]) -> int:
        points.sort()
        res = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            cur = points[i]

            if cur[0] <= prev[1]:
                res -= 1
                prev = [cur[0], min(cur[1], prev[1])]
            else:
                prev = cur

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.find_min_arrow_shots,
        ]

    def test_find_min_arrow_shots(self):
        test_cases = [
            {
                "name": "basecase",
                "points": [[10, 16], [2, 8], [1, 6], [7, 12]],
                "expected": 2,
            },
            {
                "name": "basecase",
                "points": [[1, 2], [3, 4], [5, 6], [7, 8]],
                "expected": 4,
            }
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(method=method.__name__, points=case["points"]):
                    result = method(case["points"])
                    self.assertEqual(result, case["expected"])
