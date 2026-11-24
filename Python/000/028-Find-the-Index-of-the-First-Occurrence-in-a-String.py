import unittest


class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                is_find = True
                for j in range(len(needle)):
                    if not haystack[i + j] == needle[j]:
                        is_find = False
                        break
                if is_find:
                    return i
        return -1

    def str_str2(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1
        else:
            return haystack.index(needle)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.methods = [
            cls.solution.str_str,
            cls.solution.str_str2,
        ]

        cls.test_cases = [
            ("sadbutsad", "sad", 0),
            ("leetcode", "leeto", -1),
            ("hello", "ll", 2),
            ("hello", "lo", 3),
            ("hello", "hello", 0),
            ("hello", "world", -1),
            ("aaaaa", "aaa", 0),
            ("mississippi", "issip", 4),
            ("abc", "c", 2),
            ("abc", "d", -1),
            ("a", "a", 0),
            ("a", "b", -1),
            ("a", "aa", -1),
            ("abc", "abcd", -1),
            ("aaaab", "aab", 2),
            ("abababc", "ababc", 2),
        ]

    def test_str_str(self):
        for method in self.methods:
            for haystack, needle, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        haystack=haystack,
                        needle=needle,
                ):
                    self.assertEqual(
                        method(haystack, needle),
                        expected,
                    )
