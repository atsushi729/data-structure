class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
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