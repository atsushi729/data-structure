from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = float("inf")

        while start < end:
            mid = (start + end) // 2
            curr_min = min(curr_min, nums[mid])

            # right has the min
            if nums[mid] > nums[end]:
                start = mid + 1

            # left has the  min
            else:
                end = mid - 1

        return min(curr_min, nums[start])


if __name__ == "__main__":
    s = Solution()
    import random

    nums = [random.randint(0, 100) for _ in range(10)]
    print(s.findMin(nums))
