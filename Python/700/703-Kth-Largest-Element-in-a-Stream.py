import heapq
from typing import List
import unittest


#################### Solution ####################
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        """
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        """
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]


class KthLargestV2:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        Time Complexity: O(logk)
        Space Complexity: O(k)
        """
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


#################### Test Case ####################
class TestKthLargest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_cases = [
            {
                "k": 3,
                "nums": [4, 5, 8, 2],
                "operations": [3, 5, 10, 9, 4],
                "expected": [4, 5, 5, 8, 8],
            },
            {
                "k": 1,
                "nums": [],
                "operations": [-3, -2, -4, 0, 4],
                "expected": [-3, -2, -2, 0, 4],
            },
            {
                "k": 2,
                "nums": [0],
                "operations": [-1, 1, -2, 3],
                "expected": [-1, 0, 0, 1],
            },
        ]

        cls.implementations = [
            KthLargest,
            KthLargestV2,
        ]

    def test_kth_largest(self):
        for implementation in self.implementations:
            for case in self.test_cases:
                with self.subTest(
                        implementation=implementation.__name__,
                        case=case,
                ):
                    kth_largest = implementation(
                        case["k"],
                        case["nums"].copy()
                    )

                    for value, expected in zip(
                            case["operations"],
                            case["expected"]
                    ):
                        self.assertEqual(
                            kth_largest.add(value),
                            expected
                        )
