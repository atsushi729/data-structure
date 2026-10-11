import unittest


class Solution:
    def min_rotations(self, s: str) -> int:
        res = 0
        cur_pos = 0

        for c in s:
            target = int(c)
            diff = abs(target - cur_pos)

            res += min(diff, 10 - diff)
            cur_pos = target

        return res


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.implementations = [
            self.solution.min_rotations,
        ]

    def test_min_rotations(self):
        test_cases = [
            # Basic cases
            ("123", 3),
            ("456", 6),
            ("789", 5),

            # Single digit
            ("0", 0),
            ("1", 1),
            ("5", 5),
            ("9", 1),

            # Clockwise and counterclockwise
            ("19", 3),
            ("91", 3),
            ("09", 1),
            ("90", 2),

            # Same digit repeated
            ("000", 0),
            ("111", 1),
            ("999", 1),

            # Maximum distance
            ("50", 10),
            ("05", 5),

            # Multiple rotations
            ("1234", 4),
            ("909", 3),
            ("159", 9),

            # Edge cases
            ("", 0),
            ("0000", 0),
        ]

        for func in self.implementations:
            for s, expected in test_cases:
                with self.subTest(
                        function=func.__name__,
                        s=s,
                ):
                    result = func(s)
                    self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
