import unittest


class Solution:
    def total_n_queens(self, n: int) -> int:
        col = [False] * n
        pos_dig = [False] * (n * 2)
        neg_dig = [False] * (n * 2)
        res = 0

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            for c in range(n):
                if col[c] or pos_dig[r + c] or neg_dig[r - c + n]:
                    continue
                col[c] = True
                pos_dig[r + c] = True
                neg_dig[r - c + n] = True

                backtrack(r + 1)
                col[c] = False
                pos_dig[r + c] = False
                neg_dig[r - c + n] = False

        backtrack(0)
        return res

    def total_n_queens_v2(self, n: int) -> int:
        col = set()
        pos_diag = set()
        neg_diag = set()

        def backtrack(r):
            if r == n:
                return 1
            count = 0

            for c in range(n):
                if c in col or r + c in pos_diag or r - c in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                count += backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

            return count

        return backtrack(0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.total_n_queens,
            self.solution.total_n_queens_v2,
        ]

    def test_total_n_queens(self):
        test_cases = [
            (4, 2),
            (1, 1)
        ]

        for method in self.methods:
            for n, expected in test_cases:
                with self.subTest(method=method, n=n, expected=expected):
                    result = method(n)
                    self.assertEqual(result, expected)
