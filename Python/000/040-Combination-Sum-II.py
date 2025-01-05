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


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_CombinationSum2(self):
        solution = Solution()
        self.assertListEqual(solution.combination_sum2([10, 1, 2, 7, 6, 1, 5], 8),
                             [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
        self.assertListEqual(solution.combination_sum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
