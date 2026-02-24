import unittest


class Solution:
    def ship_within_days(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            capacity = (left + right) // 2

            need_days = 1
            current_load = 0

            for w in weights:
                if current_load + w > capacity:
                    need_days += 1
                    current_load = 0
                current_load += w

            if need_days <= days:
                right = capacity
            else:
                left = capacity + 1

        return left

    def ship_within_days_2(self, weights: list[int], days: int) -> int:
        res = max(weights)
        while True:
            ships = 1
            cap = res
            for w in weights:
                if cap - w < 0:
                    ships += 1
                    cap = res
                cap -= w

            if ships <= days:
                return res

            res += 1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
            ([3, 2, 2, 4, 1, 4], 3, 6),
            ([1, 2, 3, 1, 1], 4, 3),
        ]

    def test_solution(self):
        for weights, days, expected in self.test_cases:
            with self.subTest(weights=weights, days=days, expected=expected):
                self.assertEqual(self.s.ship_within_days(weights, days), expected)

    def test_solution_2(self):
        for weights, days, expected in self.test_cases:
            with self.subTest(weights=weights, days=days, expected=expected):
                self.assertEqual(self.s.ship_within_days_2(weights, days), expected)

################### Not working code ###################
# class Solution:
#     def ship_within_days(self, weights: list[int], days: int) -> int:
#         min_weight, max_weight = 1, max(weights)
#
#         while min_weight < max_weight:
#             current_capacity = min_weight + (max_weight - min_weight) // 2
#             require_ship_day = 0
#             require_cargo = []
#
#             for weight in weights:
#                 if sum(require_cargo) + weight >= current_capacity:
#                     require_cargo = []
#                     require_cargo.append(weight)
#                     require_ship_day += 1
#                 else:
#                     require_cargo.append(weight)
#
#             if require_ship_day <= days:
#                 min_weight = current_capacity + 1
#             else:
#                 max_weight = current_capacity - 1
#         return min_weight
