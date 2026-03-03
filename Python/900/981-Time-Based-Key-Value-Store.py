import unittest
from collections import defaultdict


#################### Solution ####################
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)  # {key : [value, timestamp]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


#################### Test Case ####################
class TestTimeMap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.time_map = TimeMap()
        cls.time_map.set("foo", "bar", 1)
        cls.time_map.set("foo", "bar2", 4)

    def test_get(self):
        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.assertEqual(self.time_map.get("foo", 3), "bar")
        self.assertEqual(self.time_map.get("foo", 4), "bar2")
        self.assertEqual(self.time_map.get("foo", 5), "bar2")
        self.assertEqual(self.time_map.get("bar", 1), "")
