def search(nums: list[int], target: int):

    while len(nums) >= 1:
        middle = round(len(nums) / 2) - 1
        middle_value = nums[middle]

        if target == middle_value:
            return middle
        elif target > middle_value:
            nums[0:middle + 1] = []
        elif target < middle_value:
            nums[middle + 1:-1] = []
        else:
            return -1
    return nums


nums = [int(x) for x in input().split()]
target = int(input())
print(search(nums, target))


####################
# Simple solutions #
####################
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             return -1