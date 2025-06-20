from typing import List
import unittest


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Time Complexity: O(n) where n is the length of s
        Space Complexity: O(m) where m is the number of unique characters in s
        """
        last_index = {}

        for i, c in enumerate(s):
            last_index[c] = i

        res = []
        size = end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])

            if i == end:
                res.append(size)
                size = 0

        return res

    def partitionLabels2(self, s: str) -> List[int]:
        """
        Alternative implementation with the same time and space complexity.
        """
        last = {c: i for i, c in enumerate(s)}
        result, start, end = [], 0, 0

        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(i - start + 1)
                start = i + 1

        return result

class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("ababcbacadefegdehijhklij", [9, 7, 8]),
            ("eccbbbbdec", [10]),
            ("a", [1]),
            ("ab", [1, 1]),
            ("abcde", [1, 1, 1, 1, 1]),
        ]

    def test_partition_labels(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s, expected=expected):
                result = self.solution.partitionLabels(s)
                self.assertEqual(result, expected)

    def test_partition_labels2(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s, expected=expected):
                result = self.solution.partitionLabels2(s)
                self.assertEqual(result, expected)