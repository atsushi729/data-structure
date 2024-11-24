import unittest


#################### Solution ####################
class Solution:
    def increasing_triplet(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # 最小値を更新
            elif num <= second:
                second = num  # 中間値を更新
            else:
                return True
        return False


#################### Test Case ####################
class TestIncreasingTriplet(unittest.TestCase):
    def test_increasing_triplet(self):
        nums = [1, 2, 3, 4, 5]
        self.assertTrue(Solution().increasingTriplet(nums))
        nums = [2, 4, -2, -3]
        self.assertFalse(Solution().increasing_triplet(nums))
