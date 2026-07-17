import unittest


class Solution:
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                distance = abs(seen[n] - i)
                if distance <= k:
                    return True
            seen[n] = i
        return False

    def contains_nearby_duplicate_v2(self, nums: list[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(min(n, k))
        """
        seen = set()

        for i, n in enumerate(nums):
            if n in seen:
                return True

            seen.add(n)

            if len(seen) > k:
                seen.remove(nums[i - k])

        return False

    def contains_nearby_duplicate_v3(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True

            last_seen[num] = i

        return False


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2, 3, 1], 3, True),
            ([1, 0, 1, 1], 1, True),
            ([1, 2, 3, 1, 2, 3], 2, False),
            ([], 0, False),
            ([1, 2, 3, 4, 5], 10, False),
        ]

    def test_contains_nearby_duplicate(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                result = self.s.contains_nearby_duplicate(nums, k)
                self.assertEqual(result, expected)

    def test_contains_nearby_duplicate_v2(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                result = self.s.contains_nearby_duplicate_v2(nums, k)
                self.assertEqual(result, expected)

    def test_contains_nearby_duplicate_v3(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                result = self.s.contains_nearby_duplicate_v3(nums, k)
                self.assertEqual(result, expected)
