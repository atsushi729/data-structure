import unittest


class Solution:
    def find_min_arrow_shots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

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
                "name": "overlapping_groups",
                "points": [[10, 16], [2, 8], [1, 6], [7, 12]],
                "expected": 2,
            },
            {
                "name": "no_overlap",
                "points": [[1, 2], [3, 4], [5, 6], [7, 8]],
                "expected": 4,
            },
            {
                "name": "all_overlap",
                "points": [[1, 10], [2, 9], [3, 8], [4, 7]],
                "expected": 1,
            },
            {
                "name": "single_balloon",
                "points": [[1, 2]],
                "expected": 1,
            },
            {
                "name": "touching_endpoints",
                "points": [[1, 2], [2, 3], [3, 4]],
                "expected": 2,
            },
            {
                "name": "same_intervals",
                "points": [[1, 5], [1, 5], [1, 5]],
                "expected": 1,
            },
            {
                "name": "nested_intervals",
                "points": [[1, 10], [2, 8], [3, 6], [4, 5]],
                "expected": 1,
            },
            {
                "name": "negative_coordinates",
                "points": [[-10, -5], [-7, -3], [1, 4]],
                "expected": 2,
            },
            {
                "name": "multiple_overlap_groups",
                "points": [[1, 4], [2, 5], [6, 8], [7, 9], [10, 12]],
                "expected": 3,
            },
            {
                "name": "one_interval_connects_multiple",
                "points": [[1, 5], [2, 3], [4, 6]],
                "expected": 2,
            },
            {
                "name": "large_coordinates",
                "points": [
                    [-2147483648, 2147483647],
                    [0, 1],
                    [2, 3],
                ],
                "expected": 2,
            },
            {
                "name": "empty",
                "points": [],
                "expected": 0,
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        name=case["name"],
                        points=case["points"],
                ):
                    result = method(case["points"].copy())
                    self.assertEqual(result, case["expected"])


if __name__ == "__main__":
    unittest.main()
