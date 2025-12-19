from typing import List
import unittest


class Solution:
    def find_closest_elements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l:r + 1]

    def find_closest_elements_v2(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda num: (abs(num - x), num))
        return sorted(arr[:k])


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
            ([1, 3, 5, 7, 9], 3, 6, [3, 5, 7]),
            ([2, 4, 6, 8, 10], 2, 5, [4, 6]),
            ([0, 1, 2, 3, 4], 3, 2, [1, 2, 3]),
        ]

    def test_find_closest_elements(self):
        for arr, k, x, expected in self.test_cases:
            with self.subTest(arr=arr, k=k, x=x, expected=expected):
                self.assertEqual(self.s.find_closest_elements(arr, k, x), expected)

    def test_find_closest_elements_v2(self):
        for arr, k, x, expected in self.test_cases:
            with self.subTest(arr=arr, k=k, x=x, expected=expected):
                self.assertEqual(self.s.find_closest_elements_v2(arr, k, x), expected)
