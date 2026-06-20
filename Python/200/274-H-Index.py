import unittest


class Solution:
    def h_index(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break
        return h


class TestSolution(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([3, 0, 6, 1, 5], 3),
            ([1, 3, 1], 1),
            ([0, 0, 0], 0),
            ([10, 8, 5, 4, 3], 4),
            ([25, 8, 5, 3, 3], 3),
        ]

    def test_h_index(self):
        for citations, expected in self.test_cases:
            with self.subTest(citations=citations):
                self.assertEqual(self.solution.h_index(citations), expected)
