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

    def max_product_v2(self, nums: List[int]) -> int:
        A = []
        cur = []
        res = float('-inf')

        for num in nums:
            res = max(res, num)
            if num == 0:
                if cur:
                    A.append(cur)
                cur = []
            else:
                cur.append(num)

        if cur:
            A.append(cur)

        for sub in A:
            negs = sum(1 for i in sub if i < 0)
            prod = 1
            need = negs if negs % 2 == 0 else negs - 1
            negs = 0
            j = 0

            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    negs += 1
                    while negs > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j += 1
                if j <= i:
                    res = max(res, prod)

        return res

    def max_product_v3(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i], cur_max * nums[i])
            cur_min = min(nums[i], cur_min * nums[i])
            res = max(res, cur_max)

        return res

    def max_product_v4(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
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

    def test_maxProduct_v2(self):
        self.assertEqual(self.sol.max_product_v2([2, 3, -2, 4]), 6)
        self.assertEqual(self.sol.max_product_v2([-2, 0, -1]), 0)
        self.assertEqual(self.sol.max_product_v2([-2]), -2)
        self.assertEqual(self.sol.max_product_v2([0, 2]), 2)
        self.assertEqual(self.sol.max_product_v2([0, 2, 0]), 2)

    def test_maxProduct_v3(self):
        self.assertEqual(self.sol.max_product_v3([2, 3, -2, 4]), 6)
        self.assertEqual(self.sol.max_product_v3([-2, 0, -1]), 0)
        self.assertEqual(self.sol.max_product_v3([-2]), -2)
        self.assertEqual(self.sol.max_product_v3([0, 2]), 2)
        self.assertEqual(self.sol.max_product_v3([0, 2, 0]), 2)

    def test_maxProduct_v4(self):
        self.assertEqual(self.sol.max_product_v4([2, 3, -2, 4]), 6)
        self.assertEqual(self.sol.max_product_v4([-2, 0, -1]), 0)
        self.assertEqual(self.sol.max_product_v4([-2]), -2)
        self.assertEqual(self.sol.max_product_v4([0, 2]), 2)
        self.assertEqual(self.sol.max_product_v4([0, 2, 0]), 2)
