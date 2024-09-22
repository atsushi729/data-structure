import unittest


def group_anagram(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return list(anagrams.values())


class TestGroupAnagram(unittest.TestCase):
    def test_group_anagram(self):
        assert group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'],
                                                                             ['bat']]


""" Test cases """
test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

""" Execute the function """
print(group_anagram(test_strs))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
