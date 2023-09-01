class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []

        if len(nums1) == 0:
            return ans

        for i in nums1:
            index = nums2.index(i)
            tmp = nums2[index:]
            is_append = False

            for j in tmp:
                if j > i:
                    ans.append(j)
                    is_append = True
                    break

            if not is_append:
                ans.append(-1)

        return ans