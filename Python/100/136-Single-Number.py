from typing import List
import unittest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        answer = 0

        for num in nums:
            answer ^= num

        return answer

    def singleNumber_v2(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return next(iter(seen))

    def singleNumber_v3(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            flag = True

            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    flag = False
                    break

            if flag:
                return nums[i]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([2, 2, 1], 1),
            ([4, 1, 2, 1, 2], 4),
            ([1], 1),
            ([0, 0, 1], 1),
            ([5, 5, 6], 6),
            ([-1, -1, -2], -2),
            ([-3, 2, 2], -3),
            ([0], 0),
            ([10000, 1, 1], 10000),
            ([1, 2, 3, 4, 3, 2, 1], 4),
        ]

    def test_single_number(self):
        methods = [
            self.solution.singleNumber,
            self.solution.singleNumber_v2,
            self.solution.singleNumber_v3,
        ]

        for method in methods:
            for nums, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        nums=nums
                ):
                    self.assertEqual(
                        method(nums),
                        expected
                    )


if __name__ == "__main__":
    unittest.main()
