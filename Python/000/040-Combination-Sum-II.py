from typing import List
import unittest


#################### Solution ####################
class Solution:
    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Include the current number
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            # Skip the same number (Not include the current number)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    def combination_sum2_v2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return
            if i >= len(candidates) or total > target:
                return

            # Include the current number
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return [list(r) for r in res]


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.methods = [
            cls.solution.combination_sum2,
            cls.solution.combination_sum2_v2,
        ]

        cls.test_cases = [
            (
                [10, 1, 2, 7, 6, 1, 5], 8,
                [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
            ),
            (
                [2, 5, 2, 1, 2], 5,
                [[1, 2, 2], [5]]
            ),
            ([1, 1, 1, 1], 2, [[1, 1]]),
            ([1, 2, 3], 7, []),
            ([1], 1, [[1]]),
            ([2], 1, []),
            ([3, 3, 3, 3], 6, [[3, 3]]),
            ([1, 2, 3, 4, 5], 5, [[1, 4], [2, 3], [5]]),
        ]

    def test_combination_sum2(self):
        for method in self.methods:
            for candidates, target, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        candidates=candidates,
                        target=target
                ):
                    self.assertListEqual(
                        sorted(method(candidates.copy(), target)),
                        sorted(expected)
                    )


if __name__ == "__main__":
    unittest.main()
