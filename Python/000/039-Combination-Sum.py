import unittest
from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    def combination_sum_v2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(candidates)):
                if total + candidates[j] <= target:
                    cur.append(candidates[j])
                    dfs(j, cur, total + candidates[j])
                    cur.pop()

        dfs(0, [], 0)
        return res

    def combination_sum_v3(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        current = []

        def backtrack(start, remain):
            if remain == 0:
                combinations.append(current[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, remain - candidates[i])
                current.pop()

        backtrack(0, target)
        return combinations


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.combination_sum,
            self.solution.combination_sum_v2,
            self.solution.combination_sum_v3,
        ]

        self.test_cases = [
            (
                [2, 3, 6, 7],
                7,
                [[2, 2, 3], [7]],
            ),
            (
                [2, 3, 5],
                8,
                [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            ),
            (
                [2],
                1,
                [],
            ),
            (
                [1],
                2,
                [[1, 1]],
            ),
        ]

    def test_combination_sum(self):
        for method in self.methods:
            for candidates, target, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        candidates=candidates,
                        target=target,
                ):
                    actual = method(candidates, target)

                    actual = sorted([sorted(x) for x in actual])
                    expected_sorted = sorted([sorted(x) for x in expected])

                    self.assertEqual(actual, expected_sorted)
