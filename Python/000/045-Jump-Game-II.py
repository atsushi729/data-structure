import unittest


class Solutions:
    def jump(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res


class TestSolutions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solutions()
        cls.test_cases = [
            ([2, 3, 1, 1, 4], 2),
            ([2, 3, 0, 1, 4], 2),
            ([0], 0),
            ([1, 0], 1),
            ([2, 0, 0], 1),
            ([1, 2, 3], 2),
        ]

    def test_jump_with_query(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.solution.jump(nums)
                self.assertEqual(result, expected)
