import unittest
import heapq


#################### Solution ####################
class MedianFinder:

    def __init__(self):
        self.data = []

    def add_num(self, num: int) -> None:
        self.data.append(num)

    def find_median(self) -> float:
        self.data.sort()
        n = len(self.data)
        if n & 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2] + self.data[n // 2 - 1]) / 2


class MedianFinderV2:

    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def find_median(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return float(self.large[0])


#################### Test Case ####################
class TestMedianFinder(unittest.TestCase):
    def test_find_median(self):
        median_finder = MedianFinder()
        median_finder.add_num(1)
        median_finder.add_num(2)
        self.assertEqual(median_finder.find_median(), 1.5)
        median_finder.add_num(3)
        self.assertEqual(median_finder.find_median(), 2.0)
        median_finder.add_num(4)
        self.assertEqual(median_finder.find_median(), 2.5)
        median_finder.add_num(0)
        self.assertEqual(median_finder.find_median(), 2.0)

    def test_find_median_v2(self):
        median_finder = MedianFinderV2()
        median_finder.add_num(1)
        median_finder.add_num(2)
        self.assertEqual(median_finder.find_median(), 1.5)
        median_finder.add_num(3)
        self.assertEqual(median_finder.find_median(), 2.0)
        median_finder.add_num(4)
        self.assertEqual(median_finder.find_median(), 2.5)
        median_finder.add_num(0)
        self.assertEqual(median_finder.find_median(), 2.0)
