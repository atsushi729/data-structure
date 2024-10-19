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


def model_eval_rpn(tokens: list[str]) -> int:
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


class TestEvalRPN(unittest.TestCase):
    def test_eval_rpn(self):
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(eval_rpn(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

    def test_model_eval_rpn(self):
        self.assertEqual(model_eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(model_eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(model_eval_rpn(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
