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
