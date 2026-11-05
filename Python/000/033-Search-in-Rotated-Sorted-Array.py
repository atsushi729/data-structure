import unittest


#################### Solution ####################
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

    def search_v2(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Left portion is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Right portion is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


#################### Test Case ####################
class TestSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.search,
            self.solution.search_v2,
        ]

        self.test_cases = [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
            ([1], 1, 0),
            ([], 1, -1),
            ([1, 2, 3, 4, 5], 3, 2),
            ([1, 2, 3, 4, 5], 6, -1),
            ([3, 4, 5, 1, 2], 3, 0),
            ([3, 4, 5, 1, 2], 2, 4),
            ([3, 4, 5, 1, 2], 1, 3),
            ([2, 1], 2, 0),
            ([2, 1], 1, 1),
            ([2, 1], 3, -1),
            ([5, 1, 2, 3, 4], 5, 0),
            ([5, 1, 2, 3, 4], 4, 4),
            ([1, 2, 3, 4, 5], 1, 0),
            ([1, 2, 3, 4, 5], 5, 4),
        ]

    def test_search(self):
        for method in self.methods:
            for nums, target, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        nums=nums,
                        target=target,
                ):
                    result = method(nums.copy(), target)

                    self.assertEqual(
                        result,
                        expected,
                    )
