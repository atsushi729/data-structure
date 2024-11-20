import unittest


#################### Solution ####################
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    answer = []

    for i in range(k - 1, len(nums)):
        start = i - (k - 1)
        end = i + 1
        tmp_list_max = max(nums[start:end])
        answer.append(tmp_list_max)

    return answer


#################### Test Case ####################
class TestMaxSlidingWindow(unittest.TestCase):
    def test_max_sliding_window(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [3, 3, 5, 5, 6, 7])

