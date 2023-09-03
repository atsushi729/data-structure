class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])

            if left == right:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(s.pivotIndex(nums))
