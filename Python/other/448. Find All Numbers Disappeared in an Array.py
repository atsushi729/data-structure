class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        num_list = [i for i in range(1, len(nums) + 1)]
        ans = list(set(num_list) - set(nums))

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s.findDisappearedNumbers(nums))
