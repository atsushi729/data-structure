import unittest


#################### Solution ####################
def daily_temperatures(temperatures: list[int]) -> list[int]:
    result = []

    for i in range(len(temperatures)):
        counter = 1
        is_found = False

        for j in range(i + 1, len(temperatures)):
            # Found warmer day
            if temperatures[j] > temperatures[i]:
                result.append(counter)
                is_found = True
                break
            # Check next future day
            else:
                counter += 1

        if not is_found:
            result.append(0)

    return result


def model_daily_temperatures(temperatures: [int]) -> [int]:
    n = len(temperatures)  # Get the length of the temperatures list
    answer = [0] * n
    stack = []

    for i in range(n):
        # While the stack is not empty and the current temperature is higher than the temperature at the top of the
        # stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()  # Pop the index of the top element from the stack
            answer[j] = i - j  # Record the number of days in the answer list
        stack.append(i)  # Append the current index to the stack
    return answer


#################### Test Case ####################
class TestDailyTemperature(unittest.TestCase):
    def test_daily_temperatures(self):
        self.assertEqual(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(daily_temperatures([30, 60, 90]), [1, 1, 0])

    def test_model_daily_temperatures(self):
        self.assertEqual(model_daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(model_daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(model_daily_temperatures([30, 60, 90]), [1, 1, 0])
