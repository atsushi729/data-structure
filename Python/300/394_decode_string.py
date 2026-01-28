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

    def decode_string_v2(self, s: str) -> str:
        char_stack: list[str] = []

        for char in s:
            if char != "]":
                char_stack.append(char)
            else:
                substr_list = []
                while char_stack and char_stack[-1] != "[":
                    substr_list.append(char_stack.pop())
                substr_list.reverse()
                substr = "".join(substr_list)
                char_stack.pop()  # Remove the '['

                digit_list = []
                while char_stack and char_stack[-1].isdigit():
                    digit_list.append(char_stack.pop())
                digit_list.reverse()
                digit = "".join(digit_list)

                # Repeat the substring and push back to the stack
                char_stack.append(int(digit) * substr)
        return "".join(char_stack)


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

    def test_decode_string_v2(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(self.s.decode_string_v2(s), expected)
