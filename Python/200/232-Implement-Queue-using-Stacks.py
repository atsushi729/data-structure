import unittest


class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


class TestMyQueueCases(unittest.TestCase):
    def test_queue_operations(self):
        obj = MyQueue()
        obj.push(1)
        obj.push(2)
        self.assertEqual(obj.peek(), 1)
        self.assertEqual(obj.pop(), 1)
        self.assertFalse(obj.empty())
        obj.push(3)
        self.assertEqual(obj.peek(), 2)
        self.assertEqual(obj.pop(), 2)
        self.assertEqual(obj.pop(), 3)
        self.assertTrue(obj.empty())
