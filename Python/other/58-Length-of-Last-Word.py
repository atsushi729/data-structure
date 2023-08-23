class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        chank = s.split()
        return len(chank[-1])


if __name__ == "__main__":
    s = Solution()
    text = "Hello World"
    print(s.lengthOfLastWord(text))
