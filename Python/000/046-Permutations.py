from typing import List
import unittest


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


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_permute(self):
        solution = Solution()
        self.assertListEqual(
            sorted(solution.permute([1, 2, 3])),
            sorted([
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1]
            ])
        )
        self.assertListEqual(
            sorted(solution.permute([0, 1])),
            sorted([[0, 1], [1, 0]])
        )
        self.assertListEqual(
            sorted(solution.permute([1])),
            sorted([[1]])
        )
        self.assertListEqual(
            sorted(solution.permute([])),
            sorted([[]])
        )
