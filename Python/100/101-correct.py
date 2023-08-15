class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

    def isPalindromeV2(self, s: str) -> bool:
        if not s:
            return False

        formatted_str = [char.lower() for char in filter(str.isalnum, s)]
        left, right = 0, len(formatted_str) - 1

        while left < right:
            if formatted_str[left] != formatted_str[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindromeV3(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


if __name__ == "__main__":
    st = "A man, a plan, a canal: Panama"
    s = Solution()
    print(s.isPalindromeV3(st))
