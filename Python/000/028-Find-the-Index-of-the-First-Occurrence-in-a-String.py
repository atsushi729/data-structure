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
        cls.test_cases = [
            ("sadbutsad", "sad", 0),
            ("leetcode", "leeto", -1)
        ]

    def test_str_str(self):
        for haystack, needle, expected in self.test_cases:
            with self.subTest(haystack=haystack, needle=needle):
                self.assertEqual(self.solution.str_str(haystack, needle), expected)

    def test_convert(self):
        for haystack, needle, expected in self.test_cases:
            with self.subTest(haystack=haystack, needle=needle):
                self.assertEqual(self.solution.str_str2(haystack, needle), expected)
