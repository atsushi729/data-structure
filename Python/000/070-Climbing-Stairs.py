import unittest


#################### Solution ####################
class Solution:
    def climb_stairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n

            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)

    def climb_stairs_v2(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climb_stairs_v3(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one

    def climb_stairs_v4(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_clim_stairs(self):
        self.assertEqual(Solution().climb_stairs(2), 2)
        self.assertEqual(Solution().climb_stairs(3), 3)
        self.assertEqual(Solution().climb_stairs(4), 5)
        self.assertEqual(Solution().climb_stairs(5), 8)
        self.assertEqual(Solution().climb_stairs(6), 13)
        self.assertEqual(Solution().climb_stairs(7), 21)
        self.assertEqual(Solution().climb_stairs(8), 34)
        self.assertEqual(Solution().climb_stairs(9), 55)
        self.assertEqual(Solution().climb_stairs(10), 89)
        self.assertEqual(Solution().climb_stairs(45), 1836311903)

    def test_climb_stairs_v2(self):
        self.assertEqual(Solution().climb_stairs_v2(2), 2)
        self.assertEqual(Solution().climb_stairs_v2(3), 3)
        self.assertEqual(Solution().climb_stairs_v2(4), 5)
        self.assertEqual(Solution().climb_stairs_v2(5), 8)
        self.assertEqual(Solution().climb_stairs_v2(6), 13)
        self.assertEqual(Solution().climb_stairs_v2(7), 21)
        self.assertEqual(Solution().climb_stairs_v2(8), 34)
        self.assertEqual(Solution().climb_stairs_v2(9), 55)
        self.assertEqual(Solution().climb_stairs_v2(10), 89)
        self.assertEqual(Solution().climb_stairs_v2(45), 1836311903)

    def test_climb_stairs_v3(self):
        self.assertEqual(Solution().climb_stairs_v3(2), 2)
        self.assertEqual(Solution().climb_stairs_v3(3), 3)
        self.assertEqual(Solution().climb_stairs_v3(4), 5)
        self.assertEqual(Solution().climb_stairs_v3(5), 8)
        self.assertEqual(Solution().climb_stairs_v3(6), 13)
        self.assertEqual(Solution().climb_stairs_v3(7), 21)
        self.assertEqual(Solution().climb_stairs_v3(8), 34)

    def test_climb_stairs_v4(self):
        self.assertEqual(Solution().climb_stairs_v4(2), 2)
        self.assertEqual(Solution().climb_stairs_v4(3), 3)
        self.assertEqual(Solution().climb_stairs_v4(4), 5)
        self.assertEqual(Solution().climb_stairs_v4(5), 8)
        self.assertEqual(Solution().climb_stairs_v4(6), 13)
        self.assertEqual(Solution().climb_stairs_v4(7), 21)
