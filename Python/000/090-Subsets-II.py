from typing import List
import unittest


#################### Solution ####################
class Solution:
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(i, cur):
            res.add(tuple(cur))
            if i >= len(nums):
                return

            # Include the current number
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()

            # Skip the same number (Not include the current number)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur)

        dfs(0, [])
        return [list(r) for r in res]

    def subsets_with_dup_v2(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

    def subsets_with_dup_v3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, subset):
            res.append(subset[::])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_subsets_with_dup(self):
        solution = Solution()
        self.assertListEqual(
            sorted(solution.subsets_with_dup([1, 2, 2])),
            sorted([
                [2],
                [1],
                [1, 2, 2],
                [2, 2],
                [1, 2],
                []
            ])
        )

    def test_subsets_with_dup_v2(self):
        solution = Solution()
        self.assertListEqual(
            sorted(solution.subsets_with_dup_v2([1, 2, 2])),
            sorted([
                [2],
                [1],
                [1, 2, 2],
                [2, 2],
                [1, 2],
                []
            ])
        )

    def test_subsets_with_dup_v3(self):
        solution = Solution()
        self.assertListEqual(
            sorted(solution.subsets_with_dup_v3([1, 2, 2])),
            sorted([
                [2],
                [1],
                [1, 2, 2],
                [2, 2],
                [1, 2],
                []
            ])
        )
