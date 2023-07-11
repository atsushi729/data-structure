class Solution:
    def maxSubArray(self, nums: list[int]) -> list[int]:
        max_sum = float('-inf')
        current_sum = 0
        start = 0
        end = 0
        current_start = 0

        for i, num in enumerate(nums):
            if current_sum + num < num:
                current_sum = num
                current_start = i
            else:
                current_sum += num

            if current_sum > max_sum:
                max_sum = current_sum
                start = current_start
                end = i

        return nums[start:end + 1]


if __name__ == "__main__":
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
