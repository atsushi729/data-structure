import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i, j + 1) + dfs(i + 1, j)

        return dfs(0, 0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def test_unique_paths(self):
        self.assertEqual(self.s.uniquePaths(3, 7), 28)
        self.assertEqual(self.s.uniquePaths(3, 2), 3)
        self.assertEqual(self.s.uniquePaths(7, 3), 28)
        self.assertEqual(self.s.uniquePaths(3, 3), 6)
        self.assertEqual(self.s.uniquePaths(1, 1), 1)
        self.assertEqual(self.s.uniquePaths(1, 2), 1)
        self.assertEqual(self.s.uniquePaths(2, 1), 1)
        self.assertEqual(self.s.uniquePaths(2, 2), 2)
        self.assertEqual(self.s.uniquePaths(2, 3), 3)
        self.assertEqual(self.s.uniquePaths(3, 1), 1)


