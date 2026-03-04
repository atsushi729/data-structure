import unittest


class Solution:
    def split_array(self, nums: list[int], k: int) -> int:
        def can_split(largest):
            sub_array = 1
            cur_sum = 0

            for num in nums:
                cur_sum += num
                if cur_sum > largest:
                    sub_array += 1
                    if sub_array > k:
                        return False
                    cur_sum = num
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([7, 2, 5, 10, 8], 2, 18),
            ([1, 2, 3, 4, 5], 2, 9),
            ([1, 4, 4], 3, 4)
        ]

    def test_split_array(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                self.assertEqual(self.s.split_array(nums, k), expected)