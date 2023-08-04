class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        ans = []

        for num in nums:
            if num == val:
                continue
            ans.append(num)

        return len(ans)


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(s.removeElement(nums, val))
