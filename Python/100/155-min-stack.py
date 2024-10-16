import unittest


#################### Solution ####################
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return min(self.stack)


class ModelMinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.minStack[-1]


#################### Test Case ####################
class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.get_min(), -3)
        min_stack.pop()
        self.assertEqual(min_stack.top(), 0)
        self.assertEqual(min_stack.get_min(), -2)

    def test_model_min_stack(self):
        min_stack = ModelMinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.get_min(), -3)
        min_stack.pop()
        self.assertEqual(min_stack.top(), 0)
        self.assertEqual(min_stack.get_min(), -2)
