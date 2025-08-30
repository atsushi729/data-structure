import unittest


class Solution:
    def is_happy(self, n: int) -> bool:
        if n <= 0:
            return False

        def digit_square_sum(x: int) -> int:
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s

        slow = n
        fast = digit_square_sum(n)
        while fast != 1 and slow != fast:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(digit_square_sum(fast))
        return fast == 1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (19, True),
            (2, False),
            (1, True),
            (7, True),
            (20, False),
        ]

    def test_is_happy(self):
        for n, expected in self.test_cases:
            with self.subTest(n=n):
                result = self.solution.is_happy(n)
                self.assertEqual(result, expected)
