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

    def pivotIndexV2(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i, num in enumerate(nums):
            right_sum -= num

            if left_sum == right_sum:
                return i

            left_sum += num

        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(s.pivotIndexV2(nums))
