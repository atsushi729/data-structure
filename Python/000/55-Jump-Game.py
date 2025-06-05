from typing import List
import unittest


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

    def can_jump2(self, nums: List[int]) -> bool:
        def dfs(index: int) -> bool:
            if index >= len(nums) - 1:
                return True

            end = min(index + nums[index], len(nums) - 1)

            for jump in range(index + 1, end + 1):
                if dfs(jump):
                    return True
            return False

        return dfs(0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_case = [
            ([2, 3, 1, 1, 4], True),
            ([3, 2, 1, 0, 4], False),
            ([0], True),
            ([1, 0], True),
            ([2, 0, 0], True),
            ([1, 2, 3], True),
            ([2, 5, 0, 0], True),
            ([1, 1, 1, 0], True),
            ([1, 2, 3, 4], True)
        ]

    def test_can_jump(self):
        for nums, expected in self.test_case:
            with self.subTest(nums=nums):
                result = self.solution.can_jump(nums)
                self.assertEqual(result, expected, f"Failed for input: {nums}")

    def test_can_jump2(self):
        for nums, expected in self.test_case:
            with self.subTest(nums=nums):
                result = self.solution.can_jump2(nums)
                self.assertEqual(result, expected, f"Failed for input: {nums}")
