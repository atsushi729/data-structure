class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        if not s:
            return ""

        longest_palindrome = ""
        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i + 1)

            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome


if __name__ == "__main__":
    s = Solution()
    text = "cbbd"
    print(s.longestPalindrome(text))
