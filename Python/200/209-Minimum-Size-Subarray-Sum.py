from typing import List
import unittest


class Solution:
    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        """
        Time complexity: O(N^2) where N is the length of nums
        Space complexity: O(1)
        """
        res = float('inf')
        for i in range(len(nums)):
            cur_sum = 0
            count = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                count += 1
                if cur_sum >= target:
                    res = min(res, count)
                    break
        return 0 if res == float('inf') else res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            (7, [2, 3, 1, 2, 4, 3], 2),
            (4, [1, 4, 4], 1),
            (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
            (15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 2),
        ]

    def test_minSubArrayLen(self):
        for target, nums, expected in self.test_cases:
            with self.subTest(target=target, nums=nums, expected=expected):
                self.assertEqual(self.s.min_sub_array_len(target, nums), expected)
