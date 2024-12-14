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
