import unittest


#################### Solution ####################
def find_duplicate(nums: list[int]) -> int:
    """
    Hash Set
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()

    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)
    return -1


def find_duplicate_v2(nums: list[int]) -> int:
    """
    Floyd's Tortoise and Hare (Cycle Detection)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


#################### Test Case ####################
class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = None  # 関数ベースなので不要だが形式統一のため残す

    def get_test_cases(self):
        return [
            {
                "input": [1, 3, 4, 2, 2],
                "expected": 2,
            },
            {
                "input": [3, 1, 3, 4, 2],
                "expected": 3,
            },
            {
                "input": [1, 1],
                "expected": 1,
            },
            {
                "input": [1, 1, 2],
                "expected": 1,
            },
            {
                "input": [2, 2, 2, 2, 2],
                "expected": 2,
            },
        ]

    def test_find_duplicate(self):
        """ test code for find_duplicate """
        for case in self.get_test_cases():
            with self.subTest(case=case):
                result = find_duplicate(case["input"])
                self.assertEqual(result, case["expected"])

    def test_find_duplicate_v2(self):
        """ test code for find_duplicate_v2 """
        for case in self.get_test_cases():
            with self.subTest(case=case):
                result = find_duplicate_v2(case["input"])
                self.assertEqual(result, case["expected"])
