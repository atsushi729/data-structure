import unittest


class Solution:
    def count_binary_substrings(self, s: str) -> int:
        groups = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)
        return sum(min(groups[i], groups[i + 1]) for i in range(len(groups) - 1))

    def count_binary_substrings_v2(self, s: str) -> int:
        n = len(s)
        prev, cur = 0, 1
        output = 0

        for i in range(1, n):
            if s[i] != s[i - 1]:
                output += min(cur, prev)
                prev = cur
                cur = 1
            else:
                cur += 1

        output += min(prev, cur)
        return output


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_case = [
            ("00110011", 6),
            ("10101", 4),
            ("00011100", 5),
            ("110011", 4),
            ("111000", 3),
        ]

    def test_count_binary_substrings(self):
        for s, expected in self.test_case:
            result = self.solution.count_binary_substrings(s)
            self.assertEqual(result, expected)

    def test_count_binary_substrings_v2(self):
        for s, expected in self.test_case:
            result = self.solution.count_binary_substrings_v2(s)
            self.assertEqual(result, expected)
