class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        baseCharacter = "abcdefghijklmnopqrstuvwxyz"
        counter = 0
        tmp = 0

        for i, word in enumerate(s):
            while s[i + i] == baseCharacter[i + 1]:
                tmp += 1

            counter = max(counter, tmp)
            tmp = 0

        return counter


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
