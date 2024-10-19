import unittest


def eval_rpn(tokens: list[str]) -> int:
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


class TestEvalRPN(unittest.TestCase):
    def test_eval_rpn(self):
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(eval_rpn(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
