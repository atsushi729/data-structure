import unittest


#################### Solution ####################
class Solution:
    def count_substrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # Odd case
            result += self.count_palindrome(s, i, i)
            # Even case
            result += self.count_palindrome(s, i, i + 1)
        return result

    def count_palindrome(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

    def count_substrings_v2(self, s: str) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        return count

    def count_substrings_v3(self, s: str) -> int:
        """
        Time Complexity: O(n^3)
        Space Complexity: O(1)
        """
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    count += 1
        return count

    def count_substrings_v4(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            l, r = 0, 0
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0
                       and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p

        p = manacher(s)
        res = 0
        for i in p:
            res += (i + 1) // 2
        return res


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_countSubstrings(self):
        self.assertEqual(self.solution.count_substrings('abc'), 3)
        self.assertEqual(self.solution.count_substrings('aaa'), 6)
        self.assertEqual(self.solution.count_substrings('abccba'), 9)
        self.assertEqual(self.solution.count_substrings('abccbaa'), 11)

    def test_countSubstrings_v2(self):
        self.assertEqual(self.solution.count_substrings_v2('abc'), 3)
        self.assertEqual(self.solution.count_substrings_v2('aaa'), 6)
        self.assertEqual(self.solution.count_substrings_v2('abccba'), 9)
        self.assertEqual(self.solution.count_substrings_v2('abccbaa'), 11)

    def test_countSubstrings_v3(self):
        self.assertEqual(self.solution.count_substrings_v3('abc'), 3)
        self.assertEqual(self.solution.count_substrings_v3('aaa'), 6)
        self.assertEqual(self.solution.count_substrings_v3('abccba'), 9)
        self.assertEqual(self.solution.count_substrings_v3('abccbaa'), 11)

    def test_countSubstrings_v4(self):
        self.assertEqual(self.solution.count_substrings_v4('abc'), 3)
        self.assertEqual(self.solution.count_substrings_v4('aaa'), 6)
        self.assertEqual(self.solution.count_substrings_v4('abccba'), 9)
        self.assertEqual(self.solution.count_substrings_v4('abccbaa'), 11)