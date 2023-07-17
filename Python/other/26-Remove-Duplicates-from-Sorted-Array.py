class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        position = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[position] = nums[i]
                position += 1

        return position


if __name__ == "__main__":
    solution = Solution()
    n = [1, 1, 2]
    print(solution.removeDuplicates(n))
