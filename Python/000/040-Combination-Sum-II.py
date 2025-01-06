from typing import List
import unittest


#################### Solution ####################
class Solution:
    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Include the current number
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            # Skip the same number (Not include the current number)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    def combination_sum2_v2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return
            if i >= len(candidates) or total > target:
                return

            # Include the current number
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return [list(r) for r in res]


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_CombinationSum2(self):
        solution = Solution()
        self.assertListEqual(
            sorted(solution.combination_sum2_v2([10, 1, 2, 7, 6, 1, 5], 8)),
            sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
        )
        self.assertListEqual(
            sorted(solution.combination_sum2_v2([2, 5, 2, 1, 2], 5)),
            sorted([[1, 2, 2], [5]])
        )

    def test_combinationSum2_v2(self):
        solution = Solution()
        self.assertListEqual(
            sorted(solution.combination_sum2_v2([10, 1, 2, 7, 6, 1, 5], 8)),
            sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
        )
        self.assertListEqual(
            sorted(solution.combination_sum2_v2([2, 5, 2, 1, 2], 5)),
            sorted([[1, 2, 2], [5]])
        )
