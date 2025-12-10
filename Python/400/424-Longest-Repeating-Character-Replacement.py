import unittest


#################### Solution ####################
class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            max_count = max(max_count, count[char])

            # sliding window condition
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # update the max_length
            max_length = max(max_length, right - left + 1)

        return max_length

    def model_character_replacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)

    def character_replacement_v2(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("ABAB", 2, 4),
            ("AABABBA", 1, 4),
            ("AAAA", 2, 4),
            ("ABCDE", 1, 2),
            ("AAABBC", 2, 5),
        ]

    def test_character_replacement(self):
        for s, k, expected in self.test_cases:
            with self.subTest(s=s, k=k):
                result = self.solution.character_replacement(s, k)
                self.assertEqual(result, expected)

    def test_model_character_replacement(self):
        for s, k, expected in self.test_cases:
            with self.subTest(s=s, k=k):
                result = self.solution.model_character_replacement(s, k)
                self.assertEqual(result, expected)

    def test_character_replacement_v2(self):
        for s, k, expected in self.test_cases:
            with self.subTest(s=s, k=k):
                result = self.solution.character_replacement_v2(s, k)
                self.assertEqual(result, expected)
