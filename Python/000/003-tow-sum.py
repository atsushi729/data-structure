class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

    ## Another solution
    class Solution:
        def twoSum(self, nums: list[int], target: int) -> list[int]:
            for i in range(len(nums)):
                rest = target - nums[i]
                for j in range(i + 1, len(nums)):
                    if nums[j] == rest:
                        output = [i, j]
            return output