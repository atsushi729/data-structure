class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        element_indices = {}

        for i, num in enumerate(nums):
            if num in element_indices and i - element_indices[num] <= k:
                return True
            element_indices[num] = i

        return False
