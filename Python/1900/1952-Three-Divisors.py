import math
import unittest


class Solution:
    def is_three(self, n: int) -> bool:
        """
        Time complexity: O(sqrt(n))
        Space complexity: O(1)
        """
        root = int(math.sqrt(n))
        # Check if n is a perfect square
        if root * root != n:
            return False

        # Check if root is prime
        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                return False

        # Check if root is greater than 1
        return root > 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            (4, True),
            (6, False),
            (9, True),
            (15, False),
            (25, True),
            (27, False),
            (28, False),
            (30, False),
            (49, True),
            (961, True),
            (81, False),
            (1, False),
        ]

    def test_isThree(self):
        for n, expected in self.test_cases:
            result = self.solution.is_three(n)
            self.assertEqual(result, expected)
