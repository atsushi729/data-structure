from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        if target in nums:
            return nums.index(target)

if __name__ == "__main__":
    target = 4
    nums = [30, 11, 23, 4, 20]
    s = Solution()
    ans = s.search(nums, target)
    print(ans)
