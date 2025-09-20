from typing import List
import unittest


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time complexity: O(N)
        Space complexity: O(N)
        :param intervals:
        :param newInterval:
        :return:
        """
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
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
        # Result list to store merged intervals
        res = []

        for i in range(len(intervals)):
            # Case 1: newInterval comes before the current interval (no overlap)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # Append all remaining intervals and return
                return res + intervals[i:]

            # Case 2: newInterval comes after the current interval (no overlap)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case 3: Overlapping intervals -> merge them
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # extend start
                    max(newInterval[1], intervals[i][1])  # extend end
                ]

        # Add the last newInterval after processing all intervals
        res.append(newInterval)
        return res

    def insert_v3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
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
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
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
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
            ([], [5, 7], [[5, 7]]),
            ([[1, 5]], [2, 3], [[1, 5]]),
            ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
        ]

    def test_insert(self):
        for intervals, newInterval, expected in self.test_cases:
            result = self.solution.insert(intervals, newInterval)
            self.assertEqual(result, expected)

    def test_insert_v2(self):
        for intervals, newInterval, expected in self.test_cases:
            result = self.solution.insert_v2(intervals, newInterval)
            self.assertEqual(result, expected)

    def test_insert_v3(self):
        for intervals, newInterval, expected in self.test_cases:
            result = self.solution.insert_v3(intervals, newInterval)
            self.assertEqual(result, expected)

    def test_insert_v4(self):
        for intervals, newInterval, expected in self.test_cases:
            result = self.solution.insert_v4(intervals, newInterval)
            self.assertEqual(result, expected)
