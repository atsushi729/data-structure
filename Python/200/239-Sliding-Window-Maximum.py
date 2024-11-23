import unittest
from collections import deque


#################### Solution ####################
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n * k)
    Space complexity: O(n - k + 1)
    """
    answer = []

    for i in range(k - 1, len(nums)):
        start = i - (k - 1)
        end = i + 1
        tmp_list_max = max(nums[start:end])
        answer.append(tmp_list_max)

    return answer


def max_sliding_window_v2(nums: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n)  : O(n - k + 1) Technically
    Space complexity: O(k) : Window size
    """
    output = []
    q = deque()
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output


#################### Test Case ####################
class TestMaxSlidingWindow(unittest.TestCase):
    def test_max_sliding_window(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [3, 3, 5, 5, 6, 7])

    def test_max_sliding_window_v2(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(max_sliding_window_v2(nums, k), [3, 3, 5, 5, 6, 7])
