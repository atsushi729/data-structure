import unittest


#################### Solution ####################
def generate_parenthesis(n: int) -> list:
    result = []  # Store the result

    def backtrack(current: str, open_count: int, close_count: int):
        # Base Case: Open bracket and close bracket count is equal to n
        if len(current) == 2 * n:
            result.append(current)
            return

        # Case: Open bracket can be added
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # Case: Close bracket can be added
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    # Initial call
    backtrack('', 0, 0)
    return result


def model_generate_parentheses(n: int) -> list:
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return

        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result


def generate_parenthesis_v2(n: int):
    parentheses = []
    stack = []

    def backtrack(open_p, close_p):
        if open_p == close_p == n:
            parentheses.append("".join(stack))
            return

        if open_p < n:
            stack.append("(")
            backtrack(open_p + 1, close_p)
            stack.pop()
        if close_p < open_p:
            stack.append(")")
            backtrack(open_p, close_p + 1)
            stack.pop()

    backtrack(0, 0)
    return parentheses


def generate_parenthesis_v3(n: int):
    res = [[] for _ in range(n + 1)]
    res[0] = [""]

    for k in range(1, n + 1):
        for i in range(k - 1, -1, -1):
            for left in res[i]:
                for right in res[k - i - 1]:
                    res[k].append("(" + left + ")" + right)

    return res[n]


#################### Test Case ####################
class TestGenerateParenthesis(unittest.TestCase):
    def test_generate_parenthesis(self):
        self.assertEqual(generate_parenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(generate_parenthesis(1), ["()"])

    def test_model_generate_parentheses(self):
        self.assertEqual(model_generate_parentheses(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(model_generate_parentheses(1), ["()"])

    def test_generate_parenthesis_v2(self):
        self.assertEqual(generate_parenthesis_v2(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(generate_parenthesis_v2(1), ["()"])

    def test_generate_parenthesis_v3(self):
        self.assertEqual(generate_parenthesis_v3(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(generate_parenthesis_v3(1), ["()"])
