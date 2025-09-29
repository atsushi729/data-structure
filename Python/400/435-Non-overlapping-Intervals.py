from typing import List
import unittest


class Solution:
    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        prev_end = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                res += 1
            else:
                prev_end = intervals[i][1]
        return res

    def erase_overlap_intervals_v2(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(end, prev_end)
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (
                [[1, 2], [2, 3], [3, 4], [1, 3]],
                1,
            ),
            (
                [[1, 2], [1, 2], [1, 2]],
                2,
            ),
            (
                [[1, 2], [2, 3]],
                0,
            ),
            (
                [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]],
                2,
            ),
            (
                [[1, 100], [11, 22], [1, 11], [2, 12]],
                2,
            ),
        ]

    def test_erase_overlap_intervals(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals):
                self.assertEqual(
                    self.solution.erase_overlap_intervals(intervals),
                    expected,
                )

    def test_erase_overlap_intervals_v2(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals):
                self.assertEqual(
                    self.solution.erase_overlap_intervals_v2(intervals),
                    expected,
                )
