from typing import List
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


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            # (
            #     [[1, 3], [2, 6], [8, 10], [15, 18]],
            #     [[1, 6], [8, 10], [15, 18]],
            # ),
            (
                [[1, 3], [1, 5], [6, 7]],
                [[1, 5], [6, 7]],
            ),
            # (
            #     [[1, 4], [4, 5]],
            #     [[1, 5]],
            # ),
            # (
            #     [[1, 4], [0, 2], [3, 5]],
            #     [[0, 5]],
            # ),
        ]

    def test_merge(self):
        for intervals, expected in self.test_cases:
            with self.subTest(intervals=intervals, expected=expected):
                result = self.solution.merge(intervals)
                self.assertEqual(result, expected)
