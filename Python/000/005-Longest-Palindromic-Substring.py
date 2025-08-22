import unittest
from typing import Tuple


#################### Solution ####################
class Solution:
    def longest_palindrome(self, s: str) -> str:
        """
        Expand Around Center
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> Tuple[int, int]:
            """
            s[left] と s[right] が等しい限り外側に広げる。
            戻り値: (開始インデックス, 長さ)
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            start = left + 1
            length = right - left - 1
            return start, length

        start_idx, max_len = 0, 0

        for i in range(len(s)):
            # 奇数長
            start, length = expand_around_center(i, i)
            if length > max_len:
                start_idx, max_len = start, length

            # 偶数長
            start, length = expand_around_center(i, i + 1)
            if length > max_len:
                start_idx, max_len = start, length

        return s[start_idx: start_idx + max_len]

    def longest_palindrome_v2(self, s: str) -> str:
        """
        DP（区間真偽表）
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        n = len(s)
        if n <= 1:
            return s

        res_index, res_len = 0, 1
        dp = [[False] * n for _ in range(n)]

        # 長さ1は回文
        for i in range(n):
            dp[i][i] = True

        # 長さ2以上
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > res_len:
                        res_index, res_len = i, j - i + 1

        return s[res_index: res_index + res_len]

    def longest_palindrome_v3(self, s: str) -> str:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        n = len(s)
        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]
        start, max_length = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    cur_len = j - i + 1
                    if (cur_len > max_length) or (cur_len == max_length and i < start):
                        start, max_length = i, cur_len

        return s[start:start + max_length]


#################### Test Case ####################
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

    def test_longest_palindrome_v3(self):
        self.assertEqual(self.solution.longest_palindrome_v3('babad'), 'bab')
        self.assertEqual(self.solution.longest_palindrome_v3('cbbd'), 'bb')
        self.assertEqual(self.solution.longest_palindrome_v3('c'), 'c')
        self.assertEqual(self.solution.longest_palindrome_v3('ccaaacc'), 'ccaaacc')
        self.assertIsNot(self.solution.longest_palindrome_v3('c'), 'a')
