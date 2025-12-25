import unittest
from collections import deque


#################### Solution ####################
class Solution:
    def max_sliding_window(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n * k)
        Space complexity: O(n - k + 1)
        """
        answer = []

        for i in range(k - 1, len(nums)):
            start = i - (k - 1)
            end = i + 1
            tmp_list_max = max(nums[start:end])
            answer.append(tmp_list_max)

        return answer

    def max_sliding_window_v2(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)  : O(n - k + 1) Technically
        Space complexity: O(k) : Window size
        """
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

    def max_sliding_window_v3(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n * k)
        Space complexity: O(n)
        """
        if not nums:
            return []

        output = []

        for i in range(len(nums) - k + 1):
            output.append(max(nums[i:i + k]))

        return output


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
            (([1], 1), [1]),
            (([1, -1], 1), [1, -1]),
            (([9, 11], 2), [11]),
            (([4, -2], 2), [4]),
        ]

    def test_max_sliding_window(self):
        for inputs, expected in self.test_cases:
            nums, k = inputs
            self.assertEqual(self.solution.max_sliding_window(nums, k), expected)

    def test_max_sliding_window_v2(self):
        for inputs, expected in self.test_cases:
            nums, k = inputs
            self.assertEqual(self.solution.max_sliding_window_v2(nums, k), expected)

    def test_max_sliding_window_v3(self):
        for inputs, expected in self.test_cases:
            nums, k = inputs
            self.assertEqual(self.solution.max_sliding_window_v3(nums, k), expected)
