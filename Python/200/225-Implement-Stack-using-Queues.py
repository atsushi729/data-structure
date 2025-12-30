import unittest


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


class TestMyStackCases(unittest.TestCase):
    def test_stack_operations(self):
        obj = MyStack()
        obj.push(1)
        obj.push(2)
        self.assertEqual(obj.top(), 2)
        self.assertEqual(obj.pop(), 2)
        self.assertFalse(obj.empty())
        obj.push(3)
        self.assertEqual(obj.top(), 3)
        self.assertEqual(obj.pop(), 3)
        self.assertEqual(obj.pop(), 1)
        self.assertTrue(obj.empty())
