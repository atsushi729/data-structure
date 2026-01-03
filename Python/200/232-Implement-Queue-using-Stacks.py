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


class MyQueue2:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res

    def peek(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        res = self.stack1[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res

    def empty(self) -> bool:
        return not self.stack1


class MyQueue3:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0


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

    def test_queue_v2_operations(self):
        obj = MyQueue2()
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

    def test_queue_v3_operations(self):
        obj = MyQueue3()
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
