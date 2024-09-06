class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        else:
            return False


## another solution
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


## another solution
def containsDuplicate(nums):
    sortedNum = sorted(nums)
    for i in range(len(sortedNum) - 1):
        if sortedNum[i] == sortedNum[i + 1]:
            return True
    return False


# There are two main issues with this approach:
# 1. Loss of Order:
#    - Converting a list to a set and back to a list does not preserve the original order.
#    - As a result, comparing the original list `nums` with the processed list `unique_nums` may
#      fail to detect duplicates because their orders might differ.

# 2. Inefficiency:
#    - Although the inefficiency is not the primary issue, converting the list to a set and then back to a list
#      introduces unnecessary overhead. The conversion operations themselves take additional time and memory,
#      especially for large lists.
def containsDuplicate(nums) -> bool:
    unique_nums = list(set(nums))

    if nums == unique_nums:
        return False
    return True


print(containsDuplicate([1, 2, 3]))
