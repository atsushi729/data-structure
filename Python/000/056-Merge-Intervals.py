from typing import List
from collections import defaultdict
import unittest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. 開始位置でソート
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        # 2. ループで重なり判定しながらマージ
        for start, end in intervals[1:]:
            if start <= res[-1][1]:  # 重なっている
                res[-1][1] = max(res[-1][1], end)  # 終了位置を更新
            else:
                res.append([start, end])

        return res

    def merge_v2(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1

        res = []
        intervals = []
        have = 0

        for i in sorted(mp):
            if not intervals:
                intervals.append(i)
            have += mp[i]
            if have == 0:
                intervals.append(i)
                res.append(intervals)
                intervals = []
        return res

    def merge_v3(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)

        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            res.append([interval_start, have])

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (
                [[1, 3], [2, 6], [8, 10], [15, 18]],
                [[1, 6], [8, 10], [15, 18]],
            ),
            (
                [[1, 3], [1, 5], [6, 7]],
                [[1, 5], [6, 7]],
            ),
            (
                [[1, 4], [4, 5]],
                [[1, 5]],
            ),
            (
                [[1, 4], [0, 2], [3, 5]],
                [[0, 5]],
            ),
        ]

    def test_merge(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals, expected=expected):
                result = self.solution.merge(intervals)
                self.assertEqual(result, expected)

    def test_merge_v2(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals, expected=expected):
                result = self.solution.merge_v2(intervals)
                self.assertEqual(result, expected)

    def test_merge_v3(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals, expected=expected):
                result = self.solution.merge_v3(intervals)
                self.assertEqual(result, expected)
