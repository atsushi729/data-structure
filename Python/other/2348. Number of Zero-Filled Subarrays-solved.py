class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:

        count, res = 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            res += count
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 0, 0, 2, 0, 0, 4]
    print(s.zeroFilledSubarray(nums))
