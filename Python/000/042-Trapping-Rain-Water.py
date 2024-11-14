import unittest


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        result = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        return result


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_trap(self):
        self.assertEqual(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(Solution().trap([4, 2, 0, 3, 2, 5]), 9)
