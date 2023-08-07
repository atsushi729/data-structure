class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]

        if len(nums) == 1:
            ans.append([nums[0]])
            return ans

        for i in range(len(nums)):
            ans.append([nums[i]])

        for i in range(len(nums)):
            next = i + 1

            while next < len(nums):
                ans.append([nums[i], nums[next]])
                next += 1

        if len(nums) > 2:
            ans.append([x for x in nums])

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [0]
    print(s.subsets(nums))
