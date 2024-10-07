import unittest
import collections


#################### Solution ####################
def group_anagram(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return list(anagrams.values())


# Another solution
def model_group_anagram(strs: list[str]) -> list[list[str]]:
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())


#################### Test Case ####################
class TestGroupAnagram(unittest.TestCase):
    def test_group_anagram(self):
        self.assertEqual(
            group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]), [['eat', 'tea', 'ate'], ['tan', 'nat'],
                                                                        ['bat']])

    def test_model_group_anagram(self):
        self.assertEqual(model_group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]), [['eat', 'tea', 'ate'],
                                                                                           ['tan', 'nat'],
                                                                                           ['bat']])
