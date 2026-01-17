import unittest

from attr import dataclass


class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        i = len(self.arr) - 2
        while i >= 0 and self.arr[i] <= price:
            i -= 1
        return len(self.arr) - i - 1


class StockSpanner2:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span


@dataclass
class PriceSpan:
    price: int
    span: int


class StockSpanner3:
    def __init__(self):
        self.stack: [PriceSpan] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1].price <= price:
            span += self.stack.pop().span
        self.stack.append(PriceSpan(price, span))
        return span


class TestStockSpanner(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_cases = [
            ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
            ([31, 41, 48, 59, 79], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 1, 1, 1, 1]),
            ([1], [1]),
            ([28, 14, 28, 35, 46, 53, 66, 80, 87, 88], [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]),
        ]

    def test_stock_spanner(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices):
                s = StockSpanner()
                for price, exp in zip(prices, expected):
                    self.assertEqual(s.next(price), exp)

    def test_stock_spanner2(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices):
                s = StockSpanner2()
                for price, exp in zip(prices, expected):
                    self.assertEqual(s.next(price), exp)

    def test_stock_spanner3(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices):
                s = StockSpanner3()
                for price, exp in zip(prices, expected):
                    self.assertEqual(s.next(price), exp)
