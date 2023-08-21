class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0

        for char in t:
            if s_index < len(s) and char == s[s_index]:
                s_index += 1

        return s_index == len(s)


if __name__ == "__main__":
    solution = Solution()
    s = "axc"
    t = "ahbgdc"
    print(solution.isSubsequence(s, t))
