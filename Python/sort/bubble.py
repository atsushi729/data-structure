from typing import List


class Solution:
    def bubble_sort(self, numbers: List[int]) -> List[int]:
        len_numbers = len(numbers)
        for i in range(len_numbers):
            for j in range(len_numbers - 1 - i):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return numbers


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 100) for i in range(10)]
    s = Solution()
    print(s.bubble_sort(nums))

### O(n^2)
