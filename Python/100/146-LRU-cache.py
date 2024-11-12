import unittest


#################### Solution ####################
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None


class LRUCacheWithLinkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Initialize a doubly linked list with dummy head and tail
        self.left, self.right = Node(None, None), Node(None, None)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            least_node = self.left.next
            self.remove(least_node)
            del self.cache[least_node.key]


#################### Test Case ####################
class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        cache = LRUCacheWithLinkedList(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
