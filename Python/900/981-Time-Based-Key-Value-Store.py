import unittest


#################### Solution ####################
class TimeMap:

    def __init__(self):
        self.key_store = {}  # key and list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.key_store.get(key, [])
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
    def test_time_map(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 1)
        self.assertEqual(time_map.get("foo", 1), "bar")
        self.assertEqual(time_map.get("foo", 3), "bar")
        time_map.set("foo", "bar2", 4)
        self.assertEqual(time_map.get("foo", 4), "bar2")
        self.assertEqual(time_map.get("foo", 5), "bar2")
