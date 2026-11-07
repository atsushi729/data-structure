import unittest


class Solution:
    # Approach 1: Two Pointers + Carry
    def add_binary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(result))

    # Approach 2: Built-in Conversion
    def add_binary_v2(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    # Approach 3: Bit Manipulation
    def add_binary_v3(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        while y:
            carry = (x & y) << 1
            x = x ^ y
            y = carry

        return bin(x)[2:]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.add_binary,
            self.solution.add_binary_v2,
            self.solution.add_binary_v3,
        ]

        self.test_cases = [
            ("11", "1", "100"),
            ("1010", "1011", "10101"),
            ("0", "0", "0"),
            ("0", "1", "1"),
            ("1", "0", "1"),
            ("1", "1", "10"),
            ("10", "10", "100"),
            ("111", "1", "1000"),
            ("1111", "1", "10000"),
            ("101", "10", "111"),
            ("1000", "1", "1001"),
            ("10101", "101", "11010"),
            ("111", "111", "1110"),
            ("100000", "1", "100001"),
            ("11111111", "1", "100000000"),
        ]

    def test_add_binary(self):
        for method in self.methods:
            for a, b, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        a=a,
                        b=b,
                ):
                    result = method(a, b)

                    self.assertEqual(
                        result,
                        expected,
                    )
