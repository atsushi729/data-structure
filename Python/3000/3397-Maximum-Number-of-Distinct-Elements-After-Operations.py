from typing import List
import unittest


class Solution:
    def max_distinct_elements(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        pre = -float("inf")

        for num in nums:
            cur = min(num + k, max(num - k, pre + 1))
            if cur > pre:
                answer += 1
                pre = cur

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([1, 2, 3, 4], 1, 4),
            ([1, 2, 3, 4], 2, 4),
            ([1, 2, 3, 4], 3, 4),
            ([1, 2, 3, 4], 4, 4),
            ([1, 2, 3, 4], 5, 4),
            ([1, 2, 3], 0, 3),
            ([1], 0, 1),
            ([], 0, 0),
            ([1, 2, 2, 3, 3, 4], 2, 6),
            ([4, 4, 4, 4], 1, 3),
        ]

    def test_max_distinct_elements(self):
        for nums, k, expected in self.test_cases:
            result = self.solution.max_distinct_elements(nums, k)
            self.assertEqual(result, expected)
