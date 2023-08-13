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


if __name__ == "__main__":
    st = "A man, a plan, a canal: Panama"
    s = Solution()
    print(s.isPalindrome(st))
