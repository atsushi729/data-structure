import unittest


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % len(self.queue)
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % len(self.queue)
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.queue)


class MyCircularQueueV2:
    def __init__(self, k: int):
        self.q = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.q) == self.k:
            return False
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.q:
            return False
        self.q.pop(0)
        return True

    def Front(self) -> int:
        if self.q:
            return self.q[0]
        return -1

    def Rear(self) -> int:
        if self.q:
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k


class TestMyCircularQueue(unittest.TestCase):
    def test_my_circular_queue(self):
        circular_queue = MyCircularQueue(3)
        self.assertEqual(circular_queue.enQueue(1), True)
        self.assertEqual(circular_queue.enQueue(2), True)
        self.assertEqual(circular_queue.enQueue(3), True)
        self.assertEqual(circular_queue.enQueue(4), False)
        self.assertEqual(circular_queue.Rear(), 3)

    def test_my_circular_queue_v2(self):
        circular_queue = MyCircularQueueV2(3)
        self.assertEqual(circular_queue.enQueue(1), True)
        self.assertEqual(circular_queue.enQueue(2), True)
        self.assertEqual(circular_queue.enQueue(3), True)
        self.assertEqual(circular_queue.enQueue(4), False)
        self.assertEqual(circular_queue.Rear(), 3)
