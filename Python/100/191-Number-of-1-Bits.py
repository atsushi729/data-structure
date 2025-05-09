import unittest


class Solution:
    def hamming_weight(self, n: int) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            (0b00000000000000000000000000001011, 3),
            (0b00000000000000000000000010000000, 1),
            (11, 3),
            (128, 1),
        ]

    def test_hamming_weight(self):
        for n, expected in self.test_cases:
            result = self.solution.hamming_weight(n)
            self.assertEqual(result, expected)
