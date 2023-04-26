class Solution:
    def lognestConsective(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 1

                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest


if __name__ == '__main__':
    s = Solution()
    s.lognestConsective([100, 4, 200, 1, 3, 2])
