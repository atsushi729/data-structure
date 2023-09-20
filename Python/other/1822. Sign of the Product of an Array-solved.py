class Solution:
    def arraySign(self, nums: list[int]) -> int:
        neg = 0
        for n in nums:
            if n == 0:
                return 0
            neg += (1 if n < 0 else 0)

        return -1 if neg % 2 else 1


if __name__ == "__main__":
    s = Solution()
    nums = [-1, -2, -3, -4, 3, 2, 1]
    print(s.arraySign(nums))
