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
            heapq.heappush(
                self.large,
                -heapq.heappushpop(self.small, -num)
            )
        else:
            heapq.heappush(
                self.small,
                -heapq.heappushpop(self.large, num)
            )

    def find_median(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return float(self.large[0])


#################### Test Case ####################
class TestMedianFinder(unittest.TestCase):

    def setUp(self):
        self.methods = [
            MedianFinder,
            MedianFinderV2,
        ]

        self.test_cases = [
            # Single element
            ([1], [1.0]),

            # Two elements
            ([1, 2], [1.0, 1.5]),

            # Ascending order
            ([1, 2, 3, 4, 5],
             [1.0, 1.5, 2.0, 2.5, 3.0]),

            # Descending order
            ([5, 4, 3, 2, 1],
             [5.0, 4.5, 4.0, 3.5, 3.0]),

            # Unsorted order
            ([3, 1, 5, 2, 4],
             [3.0, 2.0, 3.0, 2.5, 3.0]),

            # Duplicate values
            ([2, 2, 2, 2],
             [2.0, 2.0, 2.0, 2.0]),

            # Negative values
            ([-1, -2, -3, -4],
             [-1.0, -1.5, -2.0, -2.5]),

            # Mixed positive and negative
            ([-5, 10, -3, 7, 0],
             [-5.0, 2.5, -3.0, 2.0, 0.0]),

            # Zero values
            ([0, 0, 0],
             [0.0, 0.0, 0.0]),

            # Large values
            ([100000, -100000, 0],
             [100000.0, 0.0, 0.0]),

            # Repeated insertion
            ([1, 1, 2, 2, 3, 3],
             [1.0, 1.0, 1.0, 1.5, 2.0, 2.0]),
        ]

    def test_find_median(self):
        for method in self.methods:
            for nums, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        nums=nums
                ):
                    median_finder = method()

                    for num, expected_median in zip(
                            nums, expected
                    ):
                        median_finder.add_num(num)
                        self.assertEqual(
                            median_finder.find_median(),
                            expected_median
                        )
