import unittest


class Solution:
    def is_happy(self, n: int) -> bool:
        if n <= 0:
            return False

        def digit_square_sum(x: int) -> int:
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s

        slow = n
        fast = digit_square_sum(n)
        while fast != 1 and slow != fast:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(digit_square_sum(fast))
        return fast == 1

    def is_happy2(self, n: int) -> bool:
        seen = set()
        is_positive = True
        cur_n = n

        while is_positive:
            list_n = list(str(cur_n))
            cur_sum = 0

            for num in list_n:
                cur_sum += int(num) ** 2

            if cur_sum == 1:
                return True
            elif cur_sum in seen:
                return False
            else:
                seen.add(cur_sum)
                cur_n = cur_sum

    def is_happy3(self, n: int) -> bool:
        slow, fast = n, self.sum_of_sequares(n)

        while slow != fast:
            fast = self.sum_of_sequares(fast)
            fast = self.sum_of_sequares(fast)
            slow = self.sum_of_sequares(slow)
        return True if fast == 1 else False

    def sum_of_sequares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output

    def is_happy4(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1

    def is_happy5(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        power = lam = 1

        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            fast = self.sumOfSquares(fast)
            lam += 1
        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (19, True),
            (2, False),
            (1, True),
            (7, True),
            (20, False),
        ]

    def test_is_happy(self):
        for n, expected in self.test_cases:
            with self.subTest(n=n):
                result = self.solution.is_happy(n)
                self.assertEqual(result, expected)

    def test_is_happy2(self):
        for n, expected in self.test_cases:
            with self.subTest(n=n):
                result = self.solution.is_happy2(n)
                self.assertEqual(result, expected)

    def test_is_happy3(self):
        for n, expected in self.test_cases:
            with self.subTest(n=n):
                result = self.solution.is_happy3(n)
                self.assertEqual(result, expected)

    def test_is_happy4(self):
        for n, expected in self.test_cases:
            with self.subTest(n=n):
                result = self.solution.is_happy4(n)
                self.assertEqual(result, expected)

    def test_is_happy5(self):
        for n, expected in self.test_cases:
            with self.subTest(n=n):
                result = self.solution.is_happy5(n)
                self.assertEqual(result, expected)
