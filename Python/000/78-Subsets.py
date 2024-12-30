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


##################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_subsets(self):
        solution = Solution()
        self.assertListEqual(solution.subsets([1, 2, 3]), [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []])
        self.assertListEqual(solution.subsets([0]), [[0], []])
        self.assertListEqual(solution.subsets([]), [[]])
