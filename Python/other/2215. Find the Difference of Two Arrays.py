class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        num1, num2 = [], []

        for i in nums1:
            if i not in nums2 and i not in num1:
                num1.append(i)

        for i in nums2:
            if i not in nums1 and i not in num2:
                num2.append(i)

        return [num1, num2]
