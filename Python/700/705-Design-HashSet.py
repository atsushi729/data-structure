import unittest


class MyHashSet:
    def __init__(self):
        self.hash_list = []

    def add(self, key: int) -> None:
        if key not in self.hash_list:
            self.hash_list.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash_list:
            self.hash_list.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hash_list


class TestMyHashSet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hash_set = MyHashSet()
        cls.test_cases = [
            (
                [
                    ("add", 1),
                    ("add", 2),
                    ("contains", 1),
                    ("contains", 3),
                    ("add", 2),
                    ("contains", 2),
                    ("remove", 2),
                    ("contains", 2),
                ],
                [None, None, True, False, None, True, None, False],
            ),
        ]

    def test_hash_set(self):
        for operations, expected in self.test_cases:
            results = []
            for op, value in operations:
                if op == "add":
                    results.append(self.hash_set.add(value))
                elif op == "remove":
                    results.append(self.hash_set.remove(value))
                elif op == "contains":
                    results.append(self.hash_set.contains(value))
            self.assertEqual(results, expected)
