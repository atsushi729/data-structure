import unittest


#################### Solution ####################
class Solution:
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

    def model_daily_temperatures(self, temperatures: [int]) -> [int]:
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

    def daily_temperatures_v3(self, temperatures: [int]) -> [int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i
        return res


#################### Test Case ####################
class TestDailyTemperature(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
            ([30, 40, 50, 60], [1, 1, 1, 0]),
            ([30, 60, 90], [1, 1, 0]),
            ([90, 80, 70, 60], [0, 0, 0, 0]),
            ([70, 75, 72, 68, 74], [1, 0, 2, 1, 0]),
        ]

    def test_daily_temperatures(self):
        for temperatures, expected in self.test_cases:
            self.assertEqual(self.s.daily_temperatures(temperatures), expected)

    def test_model_daily_temperatures(self):
        for temperatures, expected in self.test_cases:
            self.assertEqual(self.s.model_daily_temperatures(temperatures), expected)

    def test_daily_temperatures_v3(self):
        for temperatures, expected in self.test_cases:
            self.assertEqual(self.s.daily_temperatures_v3(temperatures), expected)
