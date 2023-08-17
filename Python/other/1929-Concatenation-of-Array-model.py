class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums * 2


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 1]
    print(s.getConcatenation(nums))
