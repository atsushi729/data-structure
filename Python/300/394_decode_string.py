import unittest


class Solution:
    def decode_string(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit

                stack.append(int(digit) * substr)
        return "".join(stack)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ("3[a]2[bc]", "aaabcbc"),
            ("3[a2[c]]", "accaccacc"),
            ("2[abc]3[cd]ef", "abcabccdcdcdef"),
            ("abc3[cd]xyz", "abccdcdcdxyz"),
        ]

    def test_decode_string(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(self.s.decode_string(s), expected)
