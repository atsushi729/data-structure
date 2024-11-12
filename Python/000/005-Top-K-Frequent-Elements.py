import unittest


#################### Solution ####################
def top_k_frequent_v1(nums: [int], k: int) -> [int]:
    if not nums or not k:
        return 0

    seen = set()
    calc = {}

    for num in nums:
        if num in seen:
            calc[num] += 1
        else:
            seen.add(num)
            calc.setdefault(num, 0)
            calc[num] += 1

    sorted_dict = dict(sorted(calc.items(), key=lambda x: x[1], reverse=True))

    return list(sorted_dict.keys())[:k]


def top_k_frequent_v2(nums: [int], k: int) -> [int]:
    counter = {}

    # Count each number {1 : 1, 2 : 2, 3 : 3}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    # Sorted based on value. [(3, 3), (2, 2), (1, 1)]
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    return [item[0] for item in sorted_counter[:k]]


def top_k_frequent_v3(nums: [int], k: int) -> [int]:
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    return [item[0] for item in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]]


def model_top_k_frequent(nums: [int], k: int) -> [int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res


#################### Test Case ####################
class TestTopKFrequent(unittest.TestCase):
    def test_topKFrequent_v1(self):
        self.assertEqual(top_k_frequent_v1([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_topKFrequent_v2(self):
        self.assertEqual(top_k_frequent_v2([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_topKFrequent_v3(self):
        self.assertEqual(top_k_frequent_v3([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_model_topKFrequent(self):
        self.assertEqual(model_top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
