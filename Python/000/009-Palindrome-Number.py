import unittest


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


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_base_case(self):
        self.assertEqual(is_palindrome(121), True)

    def test_is_palindrome_fail_case(self):
        self.assertEqual(is_palindrome(-121), False)
        self.assertEqual(is_palindrome(10), False)