import unittest
import collections


#################### Solution ####################
def group_anagram(strs):
    anagrams = {}

    for s in strs:
        key = "".join(sorted(s))

        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]

    return list(anagrams.values())


def group_anagram_v2(strs: list[str]) -> list[list[str]]:
    anagrams = {}

    for s in strs:
        key = tuple(sorted(s))

        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]

    return list(anagrams.values())


def model_group_anagram(strs: list[str]) -> list[list[str]]:
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        ans[tuple(count)].append(s)

    return list(ans.values())


def group_anagram_v3(strs: list[str]) -> list[list[str]]:
    anagram_map = collections.defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())


#################### Test Case ####################
class TestGroupAnagram(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solutions = [
            group_anagram,
            group_anagram_v2,
            model_group_anagram,
            group_anagram_v3,
        ]

        cls.test_cases = [
            (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            ),
            (
                ["", ""],
                [["", ""]],
            ),
            (
                ["a"],
                [["a"]],
            ),
            (
                [],
                [],
            ),
        ]

    def test_group_anagram(self):
        for solution in self.solutions:
            for input_strs, expected in self.test_cases:
                with self.subTest(
                        solution=solution.__name__,
                        input=input_strs,
                ):
                    self.assertEqual(solution(input_strs), expected)


if __name__ == "__main__":
    unittest.main()
