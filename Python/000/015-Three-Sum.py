import unittest


#################### Solution ####################
class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]


#################### Test Case ####################
class TestThreeSum(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        self.test_cases = [
            # (nums, expected)
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
        ]

    def test_threeSum(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.s.three_sum(nums)
                result_sorted = [sorted(triplet) for triplet in result]
                expected_sorted = [sorted(triplet) for triplet in expected]
                self.assertCountEqual(result_sorted, expected_sorted)
