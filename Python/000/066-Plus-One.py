from typing import List
import unittest


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        total = result + 1
        return [int(n) for n in str(total)]

    def plus_one2(self, digits: List[int]) -> List[int]:
        digits = digits[:]
        one = 1
        i = 0
        digits.reverse()

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        digits.reverse()
        return digits

    def plus_one3(self, digits: List[int]) -> List[int]:
        digits = digits[:]
        one = 1
        i = 0
        digits.reverse()

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1

        digits.reverse()
        return digits

    def plus_one4(self, digits: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
            - Best case: O(1)  when the last digit is less than 9
            - Base case: O(k)  when the last k digits are 9
            - Worst case: O(n) when all digits are 9
        Space Complexity: O(1)
        """
        digits = digits[:]
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([1, 2, 3], [1, 2, 4]),
            ([4, 3, 2, 1], [4, 3, 2, 2]),
            ([0], [1]),
            ([9], [1, 0]),
            ([9, 9], [1, 0, 0]),
            ([1, 9, 9], [2, 0, 0]),
            ([9, 9, 9], [1, 0, 0, 0]),
        ]

    def test_plus_one(self):
        for digits, expected in self.test_cases:
            with self.subTest(digits=digits):
                result = self.solution.plus_one(digits)
                self.assertEqual(result, expected)

    def test_plus_one2(self):
        for digits, expected in self.test_cases:
            with self.subTest(digits=digits):
                result = self.solution.plus_one2(digits)
                self.assertEqual(result, expected)

    def test_plus_one3(self):
        for digits, expected in self.test_cases:
            with self.subTest(digits=digits):
                result = self.solution.plus_one3(digits)
                self.assertEqual(result, expected)

    def test_plus_one4(self):
        for digits, expected in self.test_cases:
            with self.subTest(digits=digits):
                result = self.solution.plus_one4(digits)
                self.assertEqual(result, expected)
