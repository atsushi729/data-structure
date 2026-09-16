import heapq
import unittest


class Solution:
    def k_smallest_pairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        res = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(
                heap,
                (nums1[i] + nums2[0], i, 0)
            )

        while heap and len(res) < k:
            total, i, j = heapq.heappop(heap)

            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return res

    def k_smallest_pairs_v2(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        swapped = False

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            swapped = True

        heap = []
        result = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(
                heap,
                (nums1[i] + nums2[0], i, 0)
            )

        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)

            if swapped:
                result.append([nums2[j], nums1[i]])
            else:
                result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.k_smallest_pairs,
            self.solution.k_smallest_pairs_v2
        ]

    def test_case(self):
        test_cases = [
            {
                "name": "base case",
                "nums1": [1, 7, 11],
                "nums2": [2, 4, 8],
                "k": 3,
                "expected": [
                    [1, 2],
                    [1, 4],
                    [1, 8],
                ]
            },
            {
                "name": "duplicate values",
                "nums1": [1, 1, 2],
                "nums2": [1, 2, 3],
                "k": 4,
                "expected": [
                    [1, 1],
                    [1, 1],
                    [1, 2],
                    [1, 2],
                ]
            },
            {
                "name": "empty nums1",
                "nums1": [],
                "nums2": [1, 2, 3],
                "k": 3,
                "expected": []
            },
            {
                "name": "empty nums2",
                "nums1": [1, 2, 3],
                "nums2": [],
                "k": 3,
                "expected": []
            },
            {
                "name": "k is zero",
                "nums1": [1, 2],
                "nums2": [3, 4],
                "k": 0,
                "expected": []
            },
            {
                "name": "k larger than total pairs",
                "nums1": [1, 2],
                "nums2": [3],
                "k": 5,
                "expected": [
                    [1, 3],
                    [2, 3],
                ]
            },
            {
                "name": "negative numbers",
                "nums1": [-2, -1],
                "nums2": [-3, 1],
                "k": 3,
                "expected": [
                    [-2, -3],
                    [-1, -3],
                    [-2, 1],
                ]
            }
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(method=method.__name__, case=case["name"]):
                    actual = method(
                        case["nums1"],
                        case["nums2"],
                        case["k"]
                    )

                    self.assertEqual(
                        actual,
                        case["expected"]
                    )


if __name__ == "__main__":
    unittest.main()
