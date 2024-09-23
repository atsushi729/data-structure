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


def model_longest_consecutive(nums: [int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:
            length = 1

            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)

    return longest
