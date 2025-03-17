from typing import List
import unittest


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, j):
            if i == len(nums):
                return 0

            LIS = dfs(i + 1, j)  # not include

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))  # include

            return LIS

        return dfs(0, -1)


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_lengthOfLIS(self):
        self.assertEqual(self.solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(self.solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(self.solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)
