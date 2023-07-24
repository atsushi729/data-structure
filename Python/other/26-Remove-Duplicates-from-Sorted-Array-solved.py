class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    n = [1, 1, 2]
    print(solution.removeDuplicates(n))
