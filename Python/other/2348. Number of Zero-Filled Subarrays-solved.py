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

    def zeroFilledSubarrayV2(self, nums: list[int]) -> int:
        res = 0
        temp = 0
        for i in nums:
            if i == 0:
                temp+=1
                res+=temp
            else:
                temp = 0
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 0, 0, 2, 0, 0, 4]
    print(s.zeroFilledSubarray(nums))
