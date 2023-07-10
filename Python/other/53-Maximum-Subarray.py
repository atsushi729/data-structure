class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sub_array = []
        result, current = 0, 0

        for num in nums:
            current = max(num, current + num)
            result = max(result, current)

            if result <= current:
                sub_array.append(num)
            else:
                sub_array = [num]

        return sub_array


if __name__ == "__main__":
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))