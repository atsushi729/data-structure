class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0

        for char in t:
            if s_index < len(s) and char == s[s_index]:
                s_index += 1

        return s_index == len(s)

    def isSubsequenceV2(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


if __name__ == "__main__":
    solution = Solution()
    s = "axc"
    t = "ahbgdc"
    print(solution.isSubsequenceV2(s, t))
