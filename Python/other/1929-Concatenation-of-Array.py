class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        second_list = nums[:]

        nums.extend(second_list)
        return nums


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 1]
    print(s.getConcatenation(nums))
