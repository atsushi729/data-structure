from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    def isAnagramV2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def isAnagramV3(self, s: str, t: str) -> bool:
        # If the lengths are not equal, they can't be anagrams
        if len(s) != len(t):
            return False

        # Count characters in both strings and compare
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagramV2(s, t))
