from typing import List
import unittest


class Solution:
    def find_closest_elements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Time complexity: O(N)
        Space complexity: O(1)  # excluding output
        """
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l:r + 1]

    def find_closest_elements_v2(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Time complexity: O(N log N)
        Space complexity: O(N)
        """
        arr.sort(key=lambda num: (abs(num - x), num))
        return sorted(arr[:k])

    def find_closest_elements_v3(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Time complexity: O(N + k log k)
        Space complexity: O(k)
        """
        n = len(arr)
        idx = 0
        for i in range(1, n):
            if abs(x - arr[idx]) > abs(x - arr[i]):
                idx = i
        res = [arr[idx]]
        l, r = idx - 1, idx + 1
        while len(res) < k:
            if l >= 0 and r < n:
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1
        return sorted(res)


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

    def test_find_closest_elements_v3(self):
        for arr, k, x, expected in self.test_cases:
            with self.subTest(arr=arr, k=k, x=x, expected=expected):
                self.assertEqual(self.s.find_closest_elements_v3(arr, k, x), expected)
