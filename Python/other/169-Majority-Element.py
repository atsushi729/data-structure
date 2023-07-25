class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        frequent_count = {}

        for num in nums:
            frequent_count[num] = frequent_count.get(num, 0) + 1

        return max(frequent_count.items(), key=lambda x: x[1])[0]


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(s.majorityElement(nums))