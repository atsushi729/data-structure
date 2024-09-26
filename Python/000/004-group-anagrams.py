def group_anagrams(self, strs: [str]) -> [[str]]:
    # if strs is empty, then return empty array
    if not strs[0]:
        return [[""]]

    # if list have only one element, then return itself
    if len(strs[0]) == 1:
        return strs

    # check anagram group
    ans = []
    for i in range(len(strs)):
        if self.is_anagram(strs[0], strs[i]):
            return [["ok"]]


def is_anagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
