import unittest


#################### Solution ####################
class Solution:
    def eval_rpn(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Ensure the result is an integer
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]

    def model_eval_rpn(self, tokens: list[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            (["2", "1", "+", "3", "*"], 9),
            (["4", "13", "5", "/", "+"], 6),
            (["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        ]

    def test_eval_rpn(self):
        for tokens, expected in self.test_cases:
            with self.subTest(tokens=tokens, expected=expected):
                self.assertEqual(self.s.eval_rpn(tokens), expected)

    def test_model_eval_rpn(self):
        for tokens, expected in self.test_cases:
            with self.subTest(tokens=tokens, expected=expected):
                self.assertEqual(self.s.model_eval_rpn(tokens), expected)
