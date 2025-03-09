from typing import List
import unittest


class Solution:
    def max_product(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_maxProduct(self):
        self.assertEqual(self.sol.max_product([2, 3, -2, 4]), 6)
        self.assertEqual(self.sol.max_product([-2, 0, -1]), 0)
        self.assertEqual(self.sol.max_product([-2]), -2)
        self.assertEqual(self.sol.max_product([0, 2]), 2)
        self.assertEqual(self.sol.max_product([0, 2, 0]), 2)