class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, current_sum, min_length = 0, 0, float('inf')

        for right, num in enumerate(nums):
            current_sum += num

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0


if __name__ == "__main__":
    s = Solution()
    target = 213
    nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
    print(s.minSubArrayLen(target, nums))