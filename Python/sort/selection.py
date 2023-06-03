from typing import List


class Solution:
    def selection(self, numbers: List[int]) -> List[int]:
        number_length = len(numbers)

        for i in range(number_length):
            minimum_position = i

            for j in range(i + 1, number_length):
                if numbers[minimum_position] > numbers[j]:
                    minimum_position = j

            numbers[i], numbers[minimum_position] = numbers[minimum_position], numbers[i]

        return numbers


if __name__ == "__main__":
    s = Solution()
    numbers = [2, 6, 4, 7, 12, 3, 5]
    print(s.selection(numbers))
