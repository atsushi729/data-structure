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
            n >>= 1

        return res

    def hamming_weight_v2(self, n: int) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        res = 0

        while n:
            res += n & 1
            n >>= 1

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.hamming_weight,
            self.solution.hamming_weight_v2,
        ]

        self.test_cases = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (7, 3),
            (11, 3),
            (15, 4),
            (16, 1),
            (128, 1),
            (255, 8),
            (256, 1),
            (1023, 10),
            (1024, 1),
            (0b10101010, 4),
            (0b11110000, 4),
            (0b10000001, 2),
            (0b00000000000000000000000000001011, 3),
            (0b00000000000000000000000010000000, 1),
            (0b11111111111111111111111111111101, 31),
            (0xFFFFFFFF, 32),
            (0x80000000, 1),
            (0x7FFFFFFF, 31),
        ]

    def test_hamming_weight(self):
        for method in self.methods:
            for n, expected in self.test_cases:
                with self.subTest(method=method.__name__, n=n):
                    result = method(n)
                    self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
