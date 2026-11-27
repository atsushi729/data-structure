from typing import List
import unittest


class Solution:
    def count_pairs(self, nums: List[int], target: int) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1

        return count

    def count_pairs_v2(self, nums: List[int], target: int) -> int:
        """
        Time complexity: O(n log n)
        Space complexity: O(1)
        """
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count


###################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.methods = [
            cls.solution.count_pairs,
            cls.solution.count_pairs_v2,
        ]

        cls.test_cases = [
            ([1, 2, 3, 4], 5, 2),
            ([1, 2, 3], 3, 0),
            ([1, 2, 3], 6, 3),
            ([0, -1, -2], -1, 2),
            ([-1, 1, 2, 3, 1], 2, 3),
            ([-6, 2, 5, -2, -7, -1, 3], -2, 10),
            ([1, 1, 1, 1], 3, 6),
            ([1, 1, 1, 1], 2, 0),
            ([0, 0, 0], 1, 3),
            ([-3, -2, -1], 0, 3),
            ([4, 3, 2, 1], 5, 2),
            ([], 0, 0),
            ([1], 2, 0),
            ([1, 2], 3, 0),
            ([1, 2], 4, 1),
        ]

    def test_count_pairs(self):
        for method in self.methods:
            for nums, target, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        nums=nums,
                        target=target
                ):
                    self.assertEqual(
                        method(nums.copy(), target),
                        expected
                    )
