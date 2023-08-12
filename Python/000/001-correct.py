class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 4]
    s = Solution()
    print(s.containsDuplicate(nums))

"""
Why do I use a hash map instead of an array? 
The reason is that the time complexity of a hash map is always O(1), making it more efficient compared to an array. 
Using an array would lead to a runtime error due to its time complexity of O(n), as it needs to go through all the elements in the array.
"""
