import unittest


#################### Solution ####################
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        if n & 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2] + self.data[n // 2 - 1]) / 2


#################### Test Case ####################
class TestMedianFinder(unittest.TestCase):
    def test_find_median(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(2)
        self.assertEqual(median_finder.findMedian(), 1.5)
        median_finder.addNum(3)
        self.assertEqual(median_finder.findMedian(), 2.0)
        median_finder.addNum(4)
        self.assertEqual(median_finder.findMedian(), 2.5)
        median_finder.addNum(0)
        self.assertEqual(median_finder.findMedian(), 2.0)
