import unittest


class MyHashMap:
    def __init__(self):
        self.hash_list = {}

    def put(self, key: int, value: int) -> None:
        self.hash_list[key] = value

    def get(self, key: int) -> int:
        if key in self.hash_list:
            return self.hash_list[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.hash_list:
            self.hash_list.pop(key)


class HashMapV2:
    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None


class HashMapV3:
    class MyHashMap:

        def __init__(self):
            self.map = [ListNode() for _ in range(1000)]

        def hash(self, key: int) -> int:
            return key % len(self.map)

        def put(self, key: int, value: int) -> None:
            cur = self.map[self.hash(key)]
            while cur.next:
                if cur.next.key == key:
                    cur.next.val = value
                    return
                cur = cur.next
            cur.next = ListNode(key, value)

        def get(self, key: int) -> int:
            cur = self.map[self.hash(key)].next
            while cur:
                if cur.key == key:
                    return cur.val
                cur = cur.next
            return -1

        def remove(self, key: int) -> None:
            cur = self.map[self.hash(key)]
            while cur.next:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    return
                cur = cur.next


class TestMyHashMap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hash_map = MyHashMap()
        cls.test_cases = [
            (
                [
                    ("put", 1, 1),
                    ("put", 2, 2),
                    ("get", 1),
                    ("get", 3),
                    ("put", 2, 1),
                    ("get", 2),
                    ("remove", 2),
                    ("get", 2),
                ],
                [None, None, 1, -1, None, 1, None, -1],
            ),
        ]

    def test_hash_map(self):
        for operations, expected in self.test_cases:
            results = []
            for op, *values in operations:
                if op == "put":
                    results.append(self.hash_map.put(*values))
                elif op == "get":
                    results.append(self.hash_map.get(*values))
                elif op == "remove":
                    results.append(self.hash_map.remove(*values))
            self.assertEqual(results, expected)

    def test_hash_map_v2(self):
        hash_map_v2 = HashMapV2()
        for operations, expected in self.test_cases:
            results = []
            for op, *values in operations:
                if op == "put":
                    results.append(hash_map_v2.put(*values))
                elif op == "get":
                    results.append(hash_map_v2.get(*values))
                elif op == "remove":
                    results.append(hash_map_v2.remove(*values))
            self.assertEqual(results, expected)

    def test_hash_map_v3(self):
        hash_map_v3 = HashMapV3.MyHashMap()
        for operations, expected in self.test_cases:
            results = []
            for op, *values in operations:
                if op == "put":
                    results.append(hash_map_v3.put(*values))
                elif op == "get":
                    results.append(hash_map_v3.get(*values))
                elif op == "remove":
                    results.append(hash_map_v3.remove(*values))
            self.assertEqual(results, expected)
