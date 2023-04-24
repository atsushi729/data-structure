class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        current = sorted_nums[0] - 1
        sequence = []
        ans = []
        for num in sorted_nums:
            if current + 1 == num:
                ans.append(num)
                current = num
            else:
                sequence.append(len(ans))
                current = num
                ans = []
        sequence.append(len(ans))
        return max(sequence)


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
