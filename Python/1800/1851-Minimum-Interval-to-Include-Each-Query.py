from typing import List
import unittest


class Solution:
    def min_interval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []

        for q in queries:
            cur = -1
            for l, r in intervals:
                if l <= q <= r:
                    if cur == -1 or (r - l + 1) < cur:
                        cur = r - l + 1
            res.append(cur)
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (
                [[1, 4], [2, 4], [3, 6], [4, 4]],
                [2, 3, 4, 5],
                [3, 3, 1, 4],
            ),
            (
                [[2, 3], [2, 5], [1, 8], [20, 25]],
                [2, 19, 5, 22],
                [2, -1, 4, 6],
            ),
            (
                [[1, 10], [5, 15], [10, 20]],
                [10],
                [10],
            ),
            (
                [[1, 2], [3, 4], [5, 6]],
                [7],
                [-1],
            ),
            (
                [],
                [1, 2, 3],
                [-1, -1, -1],
            ),
        ]

    def test_min_interval(self):
        for intervals, queries, expected in self.test_cases:
            with self.subTest(intervals=intervals, queries=queries):
                self.assertEqual(
                    self.solution.min_interval(intervals, queries),
                    expected,
                )
