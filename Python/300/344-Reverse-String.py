from typing import List
import unittest


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverse_string_v2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []

        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
        return s


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
            (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
            (["A"], ["A"]),
            (["A", "B"], ["B", "A"]),
            (["A", "B", "C"], ["C", "B", "A"]),
            ([], []),
            (["a", "b", "c", "d", "e", "f"], ["f", "e", "d", "c", "b", "a"]),
        ]

    def test_reverse_string(self):
        for input_data, expected in self.test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                self.assertEqual(self.s.reverse_string(input_data.copy()), expected)

    def test_reverse_string_v2(self):
        for input_data, expected in self.test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                self.assertEqual(self.s.reverse_string_v2(input_data.copy()), expected)
