class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if 0 in nums:
            return 0

        calc = nums[0]

        for i in range(1, len(nums)):
            calc = calc * nums[i]

        if calc > 0:
            return 1
        elif calc == 0:
            return 0
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    nums = [-1, -2, -3, -4, 3, 2, 1]
    print(s.arraySign(nums))
