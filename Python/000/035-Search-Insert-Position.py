import unittest


class Solution:
    def search_insert(self, nums: [int], target: int) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 7, 4),
            ([1, 3, 5, 6], 0, 0),
        ]

    def test_search_insert(self):
        for nums, target, expected in self.test_cases:
            with self.subTest(nums=nums, target=target):
                result = self.s.search_insert(nums, target)
                self.assertEqual(result, expected)
