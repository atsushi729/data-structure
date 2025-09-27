from typing import List
import unittest
import heapq


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (
                [Interval(0, 30), Interval(5, 10), Interval(15, 20)],
                2,
            ),
            (
                [Interval(7, 10), Interval(2, 4)],
                1,
            ),
            (
                [],
                0,
            ),
            (
                [Interval(1, 5), Interval(2, 6), Interval(3, 7), Interval(4, 8), Interval(5, 9)],
                4,
            ),
        ]

    def test_min_meeting_rooms(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals):
                self.assertEqual(
                    self.solution.min_meeting_rooms(intervals),
                    expected,
                )
