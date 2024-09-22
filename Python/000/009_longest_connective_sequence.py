class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        ans = 1  # initialize answer to 1, as a sequence of length 1 always exists
        current_streak = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] != sorted_nums[i - 1]:
                if sorted_nums[i] == sorted_nums[i - 1] + 1:
                    current_streak += 1
                else:
                    ans = max(ans, current_streak)
                    current_streak = 1
        return max(ans, current_streak)


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))