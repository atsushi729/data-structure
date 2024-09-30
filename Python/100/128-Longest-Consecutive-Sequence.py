def longestConsecutive(nums: list[int]) -> int:
    sorted_nums = sorted(set(nums))
    if not sorted_nums:
        return 0

    max_consecutive = 1
    current_consecutive = 1

    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            current_consecutive += 1
        else:
            max_consecutive = max(max_consecutive, current_consecutive)
            current_consecutive = 1

    max_consecutive = max(max_consecutive, current_consecutive)
    return max_consecutive
