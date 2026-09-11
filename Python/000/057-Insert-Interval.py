from copy import deepcopy
from typing import List
import unittest


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

    def insert_v2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        res.append(newInterval)
        return res

    def insert_v3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)

        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res

    def insert_v4(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        res.append(newInterval)
        return res


class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.insert,
            self.solution.insert_v2,
            self.solution.insert_v3,
            self.solution.insert_v4,
        ]

        self.test_cases = [
            (
                "merge_with_one_interval",
                [[1, 3], [6, 9]],
                [2, 5],
                [[1, 5], [6, 9]],
            ),
            (
                "merge_multiple_intervals",
                [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                [4, 8],
                [[1, 2], [3, 10], [12, 16]],
            ),
            (
                "empty_intervals",
                [],
                [5, 7],
                [[5, 7]],
            ),
            (
                "new_interval_inside_existing",
                [[1, 5]],
                [2, 3],
                [[1, 5]],
            ),
            (
                "new_interval_after_all",
                [[1, 5]],
                [6, 8],
                [[1, 5], [6, 8]],
            ),
            (
                "new_interval_before_all",
                [[3, 5], [7, 9]],
                [1, 2],
                [[1, 2], [3, 5], [7, 9]],
            ),
            (
                "merge_touching_intervals",
                [[1, 2], [5, 7]],
                [2, 5],
                [[1, 7]],
            ),
            (
                "cover_all_intervals",
                [[2, 3], [5, 7], [8, 10]],
                [1, 12],
                [[1, 12]],
            ),
        ]

    def test_insert_methods(self):
        for method in self.methods:
            for name, intervals, new_interval, expected in self.test_cases:
                with self.subTest(method=method.__name__, case=name):
                    result = method(
                        deepcopy(intervals),
                        deepcopy(new_interval),
                    )

                    self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
