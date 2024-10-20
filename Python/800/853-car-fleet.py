import unittest


#################### Solution ####################
def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []

    for p, s in pair:
        stack.append((target - p) / s)

        # If new stack is faster than top stack, then pop newest stack value (stack[-1]).
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


def model_car_fleet(target: int, position: list[int], speed: list[int]) -> int:
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


#################### Test Case ####################
class TestCarFleet(unittest.TestCase):
    def test_car_fleet(self):
        self.assertEqual(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)

    def test_model_car_fleet(self):
        self.assertEqual(model_car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)
