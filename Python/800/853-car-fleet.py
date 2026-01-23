import unittest
import math


#################### Solution ####################
class Solution:
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            stack.append((target - p) / s)

            # If new stack is faster than top stack, then pop newest stack value (stack[-1]).
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

    def model_car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            time = (target - p) / s

            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)

        return len(stack)

    def car_fleet_v3(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]

        fleets = 0
        current_time = 0

        for time in times:
            if time > current_time:
                fleets += 1
                current_time = time

        return fleets

    def car_fleet_v4(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

    def car_fleet_v5(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_dist = 0
        last_speed = 1

        for p, s in cars:
            dist = target - p

            if fleets == 0 or dist * last_speed > last_dist * s:
                fleets += 1
                last_dist = dist
                last_speed = s

        return fleets

    def car_fleet_v6(self, target: int, position: list[int], speed: list[int]) -> int:
        car_position_speed_pair = sorted(zip(position, speed), reverse=True)
        num_fleets = 0
        current_fleet_time = 0

        for p, s in car_position_speed_pair:
            time = (target - p) / s

            if time > current_fleet_time:
                num_fleets += 1
                current_fleet_time = time

        return num_fleets

    def car_fleet_v7(self, target: int, position: list[int], speed: list[int]) -> int:
        car_position_speed_pair = sorted(zip(position, speed), reverse=True)

        num_fleets = 0
        current_fleet_time = 0.0

        for p, s in car_position_speed_pair:
            time = (target - p) / s

            if time > current_fleet_time and not math.isclose(
                    time, current_fleet_time, rel_tol=1e-9, abs_tol=0.0
            ):
                num_fleets += 1
                current_fleet_time = time

        return num_fleets


#################### Test Case ####################
class TestCarFleet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
            (10, [3], [3], 1),
            (100, [0, 2, 4], [4, 2, 1], 1),
            (15, [5, 10, 14], [2, 1, 1], 2),
            (20, [0, 5, 10, 15], [1, 2, 3, 4], 4),
        ]

    def test_car_fleet(self):
        for target, position, speed, expected in self.test_cases:
            with self.subTest(target=target, position=position, speed=speed):
                self.assertEqual(
                    self.s.car_fleet(target, position, speed), expected
                )

    def test_model_car_fleet(self):
        for target, position, speed, expected in self.test_cases:
            with self.subTest(target=target, position=position, speed=speed):
                self.assertEqual(
                    self.s.model_car_fleet(target, position, speed), expected
                )

    def test_car_fleet_v3(self):
        for target, position, speed, expected in self.test_cases:
            with self.subTest(target=target, position=position, speed=speed):
                self.assertEqual(
                    self.s.car_fleet_v3(target, position, speed), expected
                )

    def test_car_fleet_v4(self):
        for target, position, speed, expected in self.test_cases:
            with self.subTest(target=target, position=position, speed=speed):
                self.assertEqual(
                    self.s.car_fleet_v4(target, position, speed), expected
                )

    def test_car_fleet_v5(self):
        for target, position, speed, expected in self.test_cases:
            with self.subTest(target=target, position=position, speed=speed):
                self.assertEqual(
                    self.s.car_fleet_v5(target, position, speed), expected
                )

    def test_car_fleet_v6(self):
        for target, position, speed, expected in self.test_cases:
            with self.subTest(target=target, position=position, speed=speed):
                self.assertEqual(
                    self.s.car_fleet_v6(target, position, speed), expected
                )

    def test_car_fleet_v7(self):
        for target, position, speed, expected in self.test_cases:
            with self.subTest(target=target, position=position, speed=speed):
                self.assertEqual(
                    self.s.car_fleet_v7(target, position, speed), expected
                )
