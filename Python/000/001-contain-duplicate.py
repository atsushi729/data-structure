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


print(containsDuplicate([1, 2, 3]))
