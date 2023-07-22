class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        resorted_nums = sorted(nums, reverse=True)
        current_sum, count = 0, 0

        for num in resorted_nums:
            current_sum += num
            count += 1

            if current_sum >= target:
                return count

        return 0


if __name__ == "__main__":
    s = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(s.minSubArrayLen(target, nums))
