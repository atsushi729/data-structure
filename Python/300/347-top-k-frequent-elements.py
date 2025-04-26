import unittest
from collections import Counter


#################### Solution ####################
def top_k_frequent(nums: [int], k: int) -> [int]:
    frequent_counter = {}

    # Map object to count frequency of nums.
    # e.g. {1 : 1, 2 : 2, 3 : 3}
    for n in nums:
        if n in frequent_counter:
            continue
        count = nums.count(n)
        frequent_counter[n] = count

    # Sorted based on value.
    # [(3, 3), (2, 2), (1, 1)]
    sorted_frequent_counter = sorted(frequent_counter.items(), key=lambda x: x[1], reverse=True)

    # Create key  which contain top k frequents value.
    top_k_frequents = [item[0] for item in sorted_frequent_counter[:k]]

    return top_k_frequents


def top_k_frequent_v2(nums: [int], k: int) -> [int]:
    # Count frequency of nums.
    # e.g. {1 : 3, 2 : 2, 3 : 1}
    frequent_counter = Counter(nums)

    # Sorted based on value.
    # [(3, 1), (2, 2), (1, 3)]
    sorted_frequent_counter = sorted(frequent_counter.items(), key=lambda x: x[1], reverse=True)

    # Create key which contain top k frequents value.
    top_k_frequents = [item[0] for item in sorted_frequent_counter[:k]]

    return top_k_frequents


#################### Test Case ####################
class TestTopKFrequent(unittest.TestCase):
    def test_top_k_frequent(self):
        self.assertEqual(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(top_k_frequent([1, 2], 2), [1, 2])

    def test_top_k_frequent_v2(self):
        self.assertEqual(top_k_frequent_v2([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(top_k_frequent_v2([1, 2], 2), [1, 2])


#################### Test via terminal ####################
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # [1, 2]
