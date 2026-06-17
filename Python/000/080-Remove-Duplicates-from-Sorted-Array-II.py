import unittest


class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            count = 1

            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_remove_duplicates(self):
        test_cases = [
            # example
            ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),

            # example 2
            ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7,
             [0, 0, 1, 1, 2, 3, 3]),

            # empty
            ([], 0, []),

            # one element
            ([1], 1, [1]),

            # two same elements
            ([1, 1], 2, [1, 1]),

            # three same elements
            ([1, 1, 1], 2, [1, 1]),

            # all same
            ([5, 5, 5, 5, 5], 2, [5, 5]),

            # no duplicates
            ([1, 2, 3, 4], 4, [1, 2, 3, 4]),

            # duplicates at beginning
            ([1, 1, 1, 2, 3, 4], 5, [1, 1, 2, 3, 4]),

            # duplicates at end
            ([1, 2, 3, 4, 4, 4], 5, [1, 2, 3, 4, 4]),

            # multiple groups
            ([1, 1, 1, 2, 2, 2, 3, 3, 3], 6,
             [1, 1, 2, 2, 3, 3]),
        ]

        for nums, expected_length, expected_nums in test_cases:
            with self.subTest(nums=nums):
                actual_nums = nums.copy()

                k = self.solution.remove_duplicates(actual_nums)

                self.assertEqual(expected_length, k)
                self.assertEqual(expected_nums, actual_nums[:k])
