from typing import List
import unittest


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Solution:
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        prev_end = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < prev_end:
                return False
            prev_end = intervals[i].end
        return True

    def can_attend_meetings_v2(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        for i in range(n):
            a = intervals[i]
            for j in range(i + 1, n):
                b = intervals[j]
                if not (a.end <= b.start or b.end <= a.start):
                    return False
        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (
                [Interval(0, 30), Interval(5, 10), Interval(15, 20)],
                False,
            ),
            (
                [Interval(7, 10), Interval(2, 4)],
                True,
            ),
            (
                [],
                True,
            ),
        ]

    def test_can_attend_meetings(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals):
                result = self.solution.can_attend_meetings(intervals)
                self.assertEqual(result, expected)

    def test_can_attend_meetings_v2(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals):
                result = self.solution.can_attend_meetings_v2(intervals)
                self.assertEqual(result, expected)
