class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        tmp_list = []

        for num in nums:
            if num in tmp_list:
                tmp_list.remove(num)
            else:
                tmp_list.append(num)

        return tmp_list[0]


if __name__ == "__main__":
    s = Solution()
    nums = [4]
    print(s.singleNumber(nums))
