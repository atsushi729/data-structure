from collections import defaultdict
import unittest


def countTriplets(arr, r):
    count = 0
    potential = defaultdict(int)
    pairs = defaultdict(int)

    for val in arr:
        count += pairs[val]
        pairs[val * r] += potential[val]
        potential[val * r] += 1

    return count


class TestCountTriplets(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 2, 4], 2, 2),
            ([1, 3, 9, 9, 27, 81], 3, 6),
            ([1, 5, 5, 25], 5, 2),
            ([1, 2, 3], 2, 0),
            ([1], 1, 0),
        ]

    def test_count_triplets(self):
        for arr, r, expected in self.test_cases:
            result = countTriplets(arr, r)
            self.assertEqual(result, expected)
