class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == "__main__":
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]
    print(sol.reverseString(s))
