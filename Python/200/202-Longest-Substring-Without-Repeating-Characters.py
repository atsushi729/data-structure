class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = {}
        start = 0
        longest = 0

        for i, c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            else:
                longest = max(longest, i - start + 1)
            seen[c] = i

        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
