class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)  # O(n)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(s.pivotIndex(nums))
