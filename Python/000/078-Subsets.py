from typing import List
import unittest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    def subsets_v2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res

    def subset_v3(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res

    def subsets_v4(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res: List[List[int]] = []
        cur: List[int] = []

        def backtrack(i: int) -> None:
            if i == n:
                res.append(cur[:])
                return
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()
            backtrack(i + 1)

        backtrack(0)
        return res


##################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_subsets(self):
        solution = Solution()
        self.assertListEqual(solution.subsets([1, 2, 3]), [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []])
        self.assertListEqual(solution.subsets([0]), [[0], []])
        self.assertListEqual(solution.subsets([]), [[]])

    def test_subset_v2(self):
        solution = Solution()
        self.assertListEqual(solution.subsets_v2([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
        self.assertListEqual(solution.subsets_v2([0]), [[], [0]])
        self.assertListEqual(solution.subsets_v2([]), [[]])

    def test_subset_v3(self):
        solution = Solution()
        self.assertListEqual(solution.subset_v3([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
        self.assertListEqual(solution.subset_v3([0]), [[], [0]])
        self.assertListEqual(solution.subset_v3([]), [[]])

    def test_subset_v4(self):
        solution = Solution()
        self.assertListEqual(solution.subsets_v4([1, 2, 3]), [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []])
        self.assertListEqual(solution.subsets_v4([0]), [[0], []])
        self.assertListEqual(solution.subsets_v4([]), [[]])
