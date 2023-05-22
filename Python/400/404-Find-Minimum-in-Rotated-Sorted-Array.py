from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenNumbers = len(nums)

        for i in range(1, lenNumbers):
            tmp = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > tmp:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = tmp
        return nums[0]


if __name__ == "__main__":
    s = Solution()
    import random

    nums = [random.randint(0, 100) for _ in range(10)]
    print(s.findMin(nums))
