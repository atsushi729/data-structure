import unittest


class Solution:
    def search_insert(self, nums: list[int], target: int) -> int:
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

    def search_insert_v2(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def search_insert_v3(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.methods = [
            "search_insert",
            "search_insert_v2",
            "search_insert_v3",
        ]

        cls.test_cases = [
            # Basic cases
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 7, 4),
            ([1, 3, 5, 6], 0, 0),

            # Empty array
            ([], 5, 0),

            # Single element
            ([1], 1, 0),
            ([1], 0, 0),
            ([1], 2, 1),

            # Boundary cases
            ([1, 3, 5, 6], 1, 0),
            ([1, 3, 5, 6], 6, 3),
            ([1, 3, 5, 6], 4, 2),

            # Two elements
            ([1, 3], 2, 1),
            ([1, 3], 3, 1),

            # Negative numbers
            ([-5, -3, -1, 0, 2], -2, 2),
            ([-5, -3, -1, 0, 2], -6, 0),
        ]

    def test_search_insert(self):
        for method_name in self.methods:
            method = getattr(self.s, method_name)

            for nums, target, expected in self.test_cases:
                with self.subTest(
                        method=method_name,
                        nums=nums,
                        target=target,
                ):
                    result = method(nums, target)
                    self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
