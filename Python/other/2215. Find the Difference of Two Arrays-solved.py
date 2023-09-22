class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        out = [[], []]

        for i in s1:
            if i not in s2:
                out[0].append(i)
        for i in s2:
            if i not in s1:
                out[1].append(i)

        return out
