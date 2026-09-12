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

    def merge_v4(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = []
        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= prev_end:
                prev_end = max(prev_end, end)
            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = start, end

        res.append([prev_start, prev_end])
        return res


import unittest
import copy


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.test_cases = [
            {
                "name": "Basic Merge",
                "intervals": [[1, 3], [2, 6], [8, 10], [15, 18]],
                "expected": [[1, 6], [8, 10], [15, 18]],
            },
            {
                "name": "Same Start",
                "intervals": [[1, 3], [1, 5], [6, 7]],
                "expected": [[1, 5], [6, 7]],
            },
            {
                "name": "Touching Intervals",
                "intervals": [[1, 4], [4, 5]],
                "expected": [[1, 5]],
            },
            {
                "name": "Unsorted Intervals",
                "intervals": [[1, 4], [0, 2], [3, 5]],
                "expected": [[0, 5]],
            },
            {
                "name": "Single Interval",
                "intervals": [[1, 5]],
                "expected": [[1, 5]],
            },
            {
                "name": "No Overlap",
                "intervals": [[1, 2], [3, 4], [5, 6]],
                "expected": [[1, 2], [3, 4], [5, 6]],
            },
            {
                "name": "Contained Interval",
                "intervals": [[1, 10], [2, 3], [4, 5]],
                "expected": [[1, 10]],
            },
        ]

    def run_test_cases(self, method):
        for case in self.test_cases:
            with self.subTest(
                    method=method.__name__,
                    case=case["name"],
            ):
                intervals = copy.deepcopy(case["intervals"])

                result = method(intervals)

                self.assertEqual(
                    result,
                    case["expected"],
                    msg=(
                        f"\n"
                        f"Method   : {method.__name__}\n"
                        f"Case     : {case['name']}\n"
                        f"Input    : {case['intervals']}\n"
                        f"Expected : {case['expected']}\n"
                        f"Actual   : {result}\n"
                    ),
                )

    def test_merge(self):
        self.run_test_cases(self.solution.merge)

    def test_merge_v2(self):
        self.run_test_cases(self.solution.merge_v2)

    def test_merge_v3(self):
        self.run_test_cases(self.solution.merge_v3)

    def test_merge_v4(self):
        self.run_test_cases(self.solution.merge_v4)


if __name__ == "__main__":
    unittest.main()
