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

    def asteroid_collision_v2(self, asteroids: List[int]) -> List[int]:
        j = -1

        for a in asteroids:
            while j >= 0 > a and asteroids[j] > 0:
                if asteroids[j] > abs(a):
                    a = 0
                    break
                elif asteroids[j] == abs(a):
                    j -= 1
                    a = 0
                    break
                else:
                    j -= 1
            if a:
                j += 1
                asteroids[j] = a

        return asteroids[:j + 1]

    def asteroid_collision_v3(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
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

    def test_asteroidCollision_v2(self):
        for asteroids, expected in self.test_cases:
            with self.subTest(asteroids=asteroids, expected=expected):
                self.assertEqual(self.s.asteroid_collision_v2(asteroids), expected)

    def test_asteroidCollision_v3(self):
        for asteroids, expected in self.test_cases:
            with self.subTest(asteroids=asteroids, expected=expected):
                self.assertEqual(self.s.asteroid_collision_v3(asteroids), expected)
