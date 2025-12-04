import unittest
from typing import List


class Solution:
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                distance = abs(seen[n] - i)
                if distance <= k:
                    return True
            seen[n] = i
        return False


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2, 3, 1], 3, True),
            ([1, 0, 1, 1], 1, True),
            ([1, 2, 3, 1, 2, 3], 2, False),
            ([], 0, False),
            ([1, 2, 3, 4, 5], 10, False),
        ]

    def test_contains_nearby_duplicate(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                result = self.s.contains_nearby_duplicate(nums, k)
                self.assertEqual(result, expected)
