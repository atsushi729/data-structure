import unittest


class Solution:
    def longest_palindrome(self, s: str) -> str:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        def expand_around_center(left, right):
            # Make sure left and right in bounce and left and right is same string
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        start_idx, max_len = 0, 0

        for i in range(len(s)):
            # Odd-length string
            start, length = expand_around_center(i, i)
            if length > max_len:
                start_idx, max_len = start, length

            # Even-length string
            start, length = expand_around_center(i, i + 1)
            if length > max_len:
                start_idx, max_len = start, length

        return s[start_idx: start_idx + max_len]

    def longest_palindrome_v2(self, s: str) -> str:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        res_index, res_len = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > res_len:
                        res_index, res_len = i, j - i + 1
        return s[res_index: res_index + res_len]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_longest_palindrome(self):
        self.assertEqual(self.solution.longest_palindrome('babad'), 'bab')
        self.assertEqual(self.solution.longest_palindrome('cbbd'), 'bb')
        self.assertEqual(self.solution.longest_palindrome('c'), 'c')
        self.assertEqual(self.solution.longest_palindrome('ccaaacc'), 'ccaaacc')
        self.assertIsNot(self.solution.longest_palindrome('c'), 'a')

    def test_longest_palindrome_v2(self):
        self.assertEqual(self.solution.longest_palindrome_v2('babad'), 'aba')
        self.assertEqual(self.solution.longest_palindrome_v2('cbbd'), 'bb')
        self.assertEqual(self.solution.longest_palindrome_v2('c'), 'c')
        self.assertEqual(self.solution.longest_palindrome_v2('ccaaacc'), 'ccaaacc')
        self.assertIsNot(self.solution.longest_palindrome_v2('c'), 'a')
