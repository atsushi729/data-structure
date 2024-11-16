import unittest


#################### Solution ####################
def kids_with_candies(candies: list[int], extraCandies: int) -> list[bool]:
    max_candy = max(candies)
    answer = []

    for candy in candies:
        if candy + extraCandies >= max_candy:
            answer.append(True)
        else:
            answer.append(False)
    return answer


#################### Test Case ####################
class TestKidsWithCandies(unittest.TestCase):
    def test_kids_with_candies(self):
        self.assertEqual(kids_with_candies([2, 3, 5, 1, 3], 3), [True, True, True, False, True])
        self.assertEqual(kids_with_candies([4, 2, 1, 1, 2], 1), [True, False, False, False, False])
        self.assertEqual(kids_with_candies([12, 1, 12], 10), [True, False, True])
