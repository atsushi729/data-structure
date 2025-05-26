from typing import List
import unittest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        answer = 0

        for num in nums:
            answer = answer ^ num
        return answer

    def singleNumber_v2(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]

    def singleNumber_v3(self, nums: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        for i in range(len(nums)):
            flag = True
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    flag = False
                    break
            if flag:
                return nums[i]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([2, 2, 1], 1),
            ([4, 1, 2, 1, 2], 4),
            ([1], 1),
            ([0, 0, 1], 1),
            ([5, 5, 6], 6),
        ]

    def test_single_number(self):
        for nums, expected in self.test_cases:
            result = self.solution.singleNumber(nums)
            self.assertEqual(result, expected)

    def test_single_number_v2(self):
        for nums, expected in self.test_cases:
            result = self.solution.singleNumber_v2(nums)
            self.assertEqual(result, expected)

    def test_single_number_v3(self):
        for nums, expected in self.test_cases:
            result = self.solution.singleNumber_v3(nums)
            self.assertEqual(result, expected)
