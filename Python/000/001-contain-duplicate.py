import unittest


#################### Solution ####################
def contains_duplicate(nums: list[int]) -> bool:
    if len(nums) != len(set(nums)):
        return True
    else:
        return False


# Another solution
def contains_duplicate_v1(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Another solution
def contains_duplicate_v2(nums):
    sortedNum = sorted(nums)
    for i in range(len(sortedNum) - 1):
        if sortedNum[i] == sortedNum[i + 1]:
            return True
    return False


"""
Why do I use a hash map instead of an array? 
The reason is that the time complexity of a hash map is always O(1), making it more efficient compared to an array. 
Using an array would lead to a runtime error due to its time complexity of O(n), as it needs to go through all the elements in the array.
"""


def model_contains_duplicate(nums: [int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


#################### Test Case ####################
class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate_v1(self):
        self.assertEqual(contains_duplicate_v1([1, 2, 3, 4, 4]), True)

    def test_not_contains_duplicate_v1(self):
        self.assertEqual(contains_duplicate_v1([1, 2, 3, 4]), False)
        self.assertEqual(contains_duplicate_v1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), False)

    def test_contains_duplicate_v2(self):
        self.assertEqual(contains_duplicate_v2([1, 2, 3, 4, 4]), True)

    def test_not_contains_duplicate_v2(self):
        self.assertEqual(contains_duplicate_v2([1, 2, 3, 4]), False)
        self.assertEqual(contains_duplicate_v2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), False)


#################### Fail Case ####################
"""
Case 1: Loss of Order

There are two main issues with this approach:
1. Loss of Order:
   - Converting a list to a set and back to a list does not preserve the original order.
   - As a result, comparing the original list `nums` with the processed list `unique_nums` may
     fail to detect duplicates because their orders might differ.

2. Inefficiency:
   - Although the inefficiency is not the primary issue, converting the list to a set and then back to a list
     introduces unnecessary overhead. The conversion operations themselves take additional time and memory,
     especially for large lists.
"""


def contains_duplicate_fail_case(nums) -> bool:
    unique_nums = list(set(nums))

    if nums == unique_nums:
        return False
    return True
