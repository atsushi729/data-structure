class Solution:
    def search(self, nums: list[int], target: int):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # m = (l + r) // 2 is also work, but it may cause overflow.

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return
        return -1
