class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum = float('-inf')
        current_sum = float('-inf')

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    solution = Solution()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [-2, -1]
    print(solution.maxSubArray(nums))
