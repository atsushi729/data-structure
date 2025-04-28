import unittest


class Solution:
    def remove_duplicate_letters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and last_occurrence[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)

        return ''.join(stack)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ("bcabc", "abc"),
            ("cbacdcbc", "acdb"),
            ("abcd", "abcd"),
            ("a", "a"),
            ("", ""),
            ("zxyabc", "zxyabc"),
        ]

    def test_remove_duplicate_letters(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                result = self.solution.remove_duplicate_letters(s)
                self.assertEqual(result, expected)
