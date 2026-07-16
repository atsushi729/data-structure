import unittest


class Solution:
    def is_happy(self, n: int) -> bool:
        if n <= 0:
            return False

        def _digit_square_sum(x: int) -> int:
            total = 0

            while x:
                x, digit = divmod(x, 10)
                total += digit * digit

            return total

        slow = n
        fast = _digit_square_sum(n)

        while fast != 1 and slow != fast:
            slow = _digit_square_sum(slow)
            fast = _digit_square_sum(_digit_square_sum(fast))

        return fast == 1

    def is_happy2(self, n: int) -> bool:
        if n <= 0:
            return False

        seen = set()
        current = n

        while True:
            current_sum = sum(int(num) ** 2 for num in str(current))

            if current_sum == 1:
                return True

            if current_sum in seen:
                return False

            seen.add(current_sum)
            current = current_sum

    def is_happy3(self, n: int) -> bool:
        if n <= 0:
            return False

        slow = n
        fast = self.sum_of_squares(n)

        while slow != fast:
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(
                self.sum_of_squares(fast)
            )

        return fast == 1

    def sum_of_squares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            output += digit ** 2
            n //= 10

        return output

    def is_happy4(self, n: int) -> bool:
        if n <= 0:
            return False

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1

    def is_happy5(self, n: int) -> bool:
        if n <= 0:
            return False

        slow = n
        fast = self.sum_of_squares(n)
        power = 1
        lam = 1

        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0

            fast = self.sum_of_squares(fast)
            lam += 1

        return fast == 1

    def is_happy6(self, n: int) -> bool:
        if n <= 0:
            return False

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_digit_square_sum(n)

        return n == 1

    def get_digit_square_sum(self, val: int) -> int:
        total = 0

        while val:
            val, digit = divmod(val, 10)
            total += digit * digit

        return total


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.methods = [
            cls.solution.is_happy,
            cls.solution.is_happy2,
            cls.solution.is_happy3,
            cls.solution.is_happy4,
            cls.solution.is_happy5,
            cls.solution.is_happy6,
        ]

        cls.test_cases = [
            (19, True),
            (2, False),
            (1, True),
            (7, True),
            (20, False),
            (0, False),
            (-1, False),
        ]

    def test_is_happy_methods(self):
        for method in self.methods:
            for n, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        n=n,
                ):
                    result = method(n)
                    self.assertEqual(result, expected)
