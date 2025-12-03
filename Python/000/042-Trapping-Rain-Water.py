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

    def trap_v2(self, height: list[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            left_max = right_max = height[i]

            for j in range(i):
                left_max = max(left_max, height[j])
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])

            res += min(left_max, right_max) - height[i]

        return res


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([1, 0, 2, 1, 0, 1, 3], 5),
            ([5, 4, 1, 2], 1),
        ]

    def test_trap(self):
        for height, expected in self.test_cases:
            with self.subTest(height=height):
                result = self.s.trap(height)
                self.assertEqual(result, expected)

    def test_trap_v2(self):
        for height, expected in self.test_cases:
            with self.subTest(height=height):
                result = self.s.trap_v2(height)
                self.assertEqual(result, expected)
