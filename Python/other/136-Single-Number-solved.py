class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0

        for n in nums:
            res = n ^ res
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1]
    print(s.singleNumber(nums))
