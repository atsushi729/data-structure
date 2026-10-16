from typing import List
import unittest


#################### Solution ####################
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

    def permute_v2(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], index: int):
        if index == len(nums):
            self.res.append(nums[:])
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.backtrack(nums, index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    def permute_v3(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms

    def permute_v4(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                if num in current:
                    continue
                current.append(num)
                backtrack()
                current.pop()

        backtrack()
        return result

    def permute_v5(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(cur):
            if len(cur) == len(nums):
                permutations.append(cur.copy())
                return

            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                backtrack(cur)
                cur.pop()

        backtrack([])
        return permutations


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.implementations = [
            self.solution.permute,
            self.solution.permute_v2,
            self.solution.permute_v3,
            self.solution.permute_v4,
            self.solution.permute_v5,
        ]

    def test_permute(self):
        test_cases = [
            (
                [1, 2, 3],
                [
                    [1, 2, 3],
                    [1, 3, 2],
                    [2, 1, 3],
                    [2, 3, 1],
                    [3, 1, 2],
                    [3, 2, 1],
                ],
            ),
            ([0, 1], [[0, 1], [1, 0]]),
            ([1], [[1]]),
            ([], [[]]),
        ]

        for func in self.implementations:
            for nums, expected in test_cases:
                with self.subTest(func=func.__name__, nums=nums):
                    result = func(nums.copy())
                    self.assertEqual(
                        sorted(result),
                        sorted(expected),
                    )


if __name__ == "__main__":
    unittest.main()
