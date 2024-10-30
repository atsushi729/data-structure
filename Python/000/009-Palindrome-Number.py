import unittest


#################### Solution ####################
def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    if x == 0:
        return True
    original_x = x
    reversed_x_list = []

    while x > 0:
        first_value = x % 10
        reversed_x_list.append(str(first_value))
        x = (x - first_value) // 10

    reversed_x = int("".join(reversed_x_list))

    return original_x == reversed_x


def is_palindrome_v2(x: int) -> bool:
    list_x = list(str(x))

    return list_x == list_x[::-1]


#################### Test Case ####################
class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_base_case(self):
        self.assertEqual(is_palindrome(121), True)

    def test_is_palindrome_fail_case(self):
        self.assertEqual(is_palindrome(-121), False)
        self.assertEqual(is_palindrome(10), False)

    def test_is_palindrome_v2_base_case(self):
        self.assertEqual(is_palindrome_v2(121), True)

    def test_is_palindrome_v2_fail_case(self):
        self.assertEqual(is_palindrome_v2(-121), False)
        self.assertEqual(is_palindrome_v2(10), False)
