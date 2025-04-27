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
