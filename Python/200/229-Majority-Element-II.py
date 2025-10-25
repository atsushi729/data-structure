from collections import defaultdict
from typing import List
import unittest


class Solution:
    def majority_element(self, nums: List[int]) -> List[int]:
        target_range = len(nums) // 3
        count_dict = defaultdict(int)
        res = []

        for num in nums:
            count_dict[num] += 1

        for key, value in count_dict.items():
            if value > target_range:
                res.append(key)

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([3, 2, 3], [3]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, 1, 1, 3, 3, 2, 2, 2], [1, 2]),
            ([2, 2], [2]),
            ([0, 0, 0], [0]),
            ([4, 4, 4, 4, 4, 4, 4], [4]),
            ([1, 2, 3, 4], []),
        ]

    def test_majority_element(self):
        for input_data, expected in self.test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                self.assertEqual(
                    sorted(self.s.majority_element(input_data)), sorted(expected)
                )