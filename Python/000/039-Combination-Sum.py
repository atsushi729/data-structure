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


class TestSolution(unittest.TestCase):
    def test_combination_sum(self):
        self.assertEqual(Solution().combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(Solution().combination_sum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    def test_combination_sum_v2(self):
        self.assertEqual(Solution().combination_sum_v2([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(Solution().combination_sum_v2([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])