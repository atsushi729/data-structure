import unittest


#################### Solution ####################
def daily_temperatures(self, temperatures: list[int]) -> list[int]:
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


#################### Test Case ####################
class TestDailyTemperature(unittest.TestCase):
    def test_daily_temperatures(self):
        self.assertEqual(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(daily_temperatures([30, 60, 90]), [1, 1, 0])
