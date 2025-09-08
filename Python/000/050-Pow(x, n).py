import unittest


class Solution:
    def my_pow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        for i in range(abs(n)):
            res *= x
        return res if n > 0 else 1 / res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (2.00000, 10, 1024.00000),
            (2.10000, 3, 9.26100),
            (2.00000, -2, 0.25000),
            (0.44528, 0, 1.00000),
        ]

    def test_myPow(self):
        for x, n, expected in self.test_cases:
            with self.subTest(x=x, n=n):
                result = self.solution.my_pow(x, n)
                self.assertAlmostEqual(result, expected, places=5)
