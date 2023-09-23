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

    def findDifferenceV2(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [set1.difference(set2), set2.difference(set1)]


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    print(s.findDifferenceV2(nums1, nums2))
