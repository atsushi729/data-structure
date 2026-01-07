import unittest


#################### Solution ####################
class Solution:
    def eval_rpn(self, tokens: list[str]) -> int:
        """
        Time complexity: O(N) where N is the length of tokens
        Space complexity: O(N) where N is the length of tokens
        """
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
        """
        Time complexity: O(N) where N is the length of tokens
        Space complexity: O(N) where N is the length of tokens
        """
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

    def eval_rpn_v2(self, tokens: list[str]) -> int:
        """
        Time complexity: O(N) where N is the length of tokens
        Space complexity: O(N) where N is the length of tokens
        """

        local = tokens[:]

        def dfs():
            token = local.pop()
            if token not in "+-*/":
                return int(token)

            right = dfs()
            left = dfs()

            if token == "+":
                return left + right
            elif token == "-":
                return left - right
            elif token == "*":
                return left * right
            elif token == "/":
                return int(left / right)

        return dfs()

    def eval_rpn_v3(self, tokens: list[str]) -> int:
        """
        Time complexity: O(N^2) where N is the length of tokens
        Space complexity: O(1)
        """
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i - 2])
                    b = int(tokens[i - 1])
                    if tokens[i] == '+':
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)
                    tokens = tokens[:i - 2] + [str(result)] + tokens[i + 1:]
                    break
        return int(tokens[0])


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

    def test_eval_rpn_v2(self):
        for tokens, expected in self.test_cases:
            with self.subTest(tokens=tokens, expected=expected):
                self.assertEqual(self.s.eval_rpn_v2(tokens), expected)

    def test_eval_rpn_v3(self):
        for tokens, expected in self.test_cases:
            with self.subTest(tokens=tokens, expected=expected):
                self.assertEqual(self.s.eval_rpn_v3(tokens), expected)
