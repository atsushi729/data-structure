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


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([2, 2, 1], 1),
            ([4, 1, 2, 1, 2], 4),
            ([1], 1),
            ([0, 0, 0, 1], 1),
            ([5, 5, 5], 5),
        ]

    def test_single_number(self):
        for nums, expected in self.test_cases:
            result = self.solution.singleNumber(nums)
            self.assertEqual(result, expected)
