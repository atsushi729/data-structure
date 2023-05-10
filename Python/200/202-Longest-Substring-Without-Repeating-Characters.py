class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        baseCharacter = "abcdefghijklmnopqrstuvwxyz"
        counter = 1
        tmp = 1
        increment = 1

        for i, word in enumerate(s):
            position = s.index(word)
            if i + increment < len(s):
                while s[i + increment] == baseCharacter[position + increment]:
                    tmp += 1
                    increment += 1
                    if i + increment >= len(s):
                        break

                counter = max(counter, tmp)
                tmp = increment = 1

        return counter


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
