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
