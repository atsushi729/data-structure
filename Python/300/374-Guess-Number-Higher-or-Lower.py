import unittest


def guess(num: int, target: int) -> int:
    # This is a mock implementation of the guess API for testing purposes.
    # In a real scenario, this function would be provided by the problem's environment.
    if num == target:
        return 0
    elif num < target:
        return 1
    else:
        return -1


class Solution:
    def guess_number(self, n: int, target: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            guess_result = guess(mid, target)

            if guess_result == 0:
                return mid
            elif guess_result == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def guess_number_v2(self, n: int, target: int) -> int:
        for num in range(1, n + 1):
            if guess(num, target) == 0:
                return num
        return -1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            (10, 6, 6),
            (1, 1, 1),
            (2, 1, 1),
            (2, 2, 2),
            (100, 50, 50),
        ]

    def test_guess_number(self):
        for n, target, expected in self.test_cases:
            with self.subTest(n=n, target=target, expected=expected):
                self.assertEqual(self.s.guess_number(n, target), expected)

    def test_guess_number_v2(self):
        for n, target, expected in self.test_cases:
            with self.subTest(n=n, target=target, expected=expected):
                self.assertEqual(self.s.guess_number_v2(n, target), expected)
