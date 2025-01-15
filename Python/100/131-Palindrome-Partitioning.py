import unittest
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current_partition = []

        def dfs(start_index):
            if start_index == len(s):
                result.append(current_partition.copy())
                return

            for end_index in range(start_index, len(s)):
                if is_palindrome(s, start_index, end_index):
                    current_partition.append(s[start_index:end_index + 1])
                    dfs(end_index + 1)
                    current_partition.pop()

        def is_palindrome(string, left, right):
            while left < right:
                if string[left] != string[right]:
                    return False

                left += 1
                right -= 1
            return True

        dfs(0)
        return result


class TestSolution(unittest.TestCase):
    def test_partition(self):
        solution = Solution()
        self.assertListEqual(
            sorted(solution.partition("aab")),
            sorted([["a", "a", "b"], ["aa", "b"]])
        )
        self.assertListEqual(
            sorted(solution.partition("a")),
            sorted([["a"]])
        )
        self.assertListEqual(
            sorted(solution.partition("ab")),
            sorted([["a", "b"]])
        )
