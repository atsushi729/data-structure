from typing import List
import unittest


class Solution:
    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([5, 10, -5], [5, 10]),
            ([8, -8], []),
            ([10, 2, -5], [10]),
            ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        ]

    def test_asteroidCollision(self):
        for asteroids, expected in self.test_cases:
            with self.subTest(asteroids=asteroids, expected=expected):
                self.assertEqual(self.s.asteroid_collision(asteroids), expected)
