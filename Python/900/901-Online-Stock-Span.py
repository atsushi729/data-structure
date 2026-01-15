import unittest


class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        i = len(self.arr) - 2
        while i >= 0 and self.arr[i] <= price:
            i -= 1
        return len(self.arr) - i - 1


class TestStockSpanner(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = StockSpanner()
        cls.test_cases = [
            ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ]

    def test_stock_spanner(self):
        for prices, expected in self.test_cases:
            s = StockSpanner()
            for price, exp in zip(prices, expected):
                self.assertEqual(s.next(price), exp)
