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


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.implementations = [
            self.solution.plus_one,
            self.solution.plus_one2,
            self.solution.plus_one3,
            self.solution.plus_one4,
        ]

    def test_plus_one(self):
        test_cases = [
            # Basic cases
            ([1, 2, 3], [1, 2, 4]),
            ([4, 3, 2, 1], [4, 3, 2, 2]),

            # Single digit
            ([0], [1]),
            ([5], [6]),
            ([9], [1, 0]),

            # Carry propagation
            ([1, 2, 9], [1, 3, 0]),
            ([1, 9, 9], [2, 0, 0]),
            ([9, 9], [1, 0, 0]),
            ([9, 9, 9], [1, 0, 0, 0]),

            # No carry
            ([1, 0, 0], [1, 0, 1]),
            ([9, 0, 0], [9, 0, 1]),
        ]

        for func in self.implementations:
            for digits, expected in test_cases:
                with self.subTest(
                        function=func.__name__,
                        digits=digits,
                ):
                    original = digits[:]
                    result = func(digits)

                    self.assertEqual(result, expected)
                    self.assertEqual(digits, original)


if __name__ == "__main__":
    unittest.main()
