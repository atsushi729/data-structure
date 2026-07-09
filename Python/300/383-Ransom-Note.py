import unittest
from collections import Counter


class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for key, count in r_count.items():
            if key not in m_count:
                return False

            target_count = m_count.get(key)
            if count > target_count:
                return False

        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("same single char", "a", "a", True),
            ("ransom longer than magazine", "ab", "a", False),
            ("different char", "b", "a", False),
        ]

    def test_can_construct(self):
        for test_name, ransomNote, magazine, expected in self.test_cases:
            with self.subTest(test_name=test_name):
                self.assertEqual(
                    self.solution.can_construct(ransomNote, magazine),
                    expected
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
