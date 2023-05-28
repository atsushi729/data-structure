from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_list = []

        while len(nums) >= 3:
            for i in range(0, len(nums)):
                for j in range(1, len(nums)):
                    for k in range(2, len(nums)):
                        if nums[i] + nums[j] + nums[k] == 0:
                            ans_list.append([nums[i], nums[j], nums[k]])
            nums.pop(0)

        return ans_list


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    ans = s.threeSum(nums)
    print(ans)

"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
