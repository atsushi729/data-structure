from typing import List


class Solution:
    def cock_tail(self, numbers: List[int]) -> List[int]:
        list_len = len(numbers)
        start = 0
        end = list_len - 1
        is_swapped = True

        while is_swapped:
            is_swapped = False

            for i in range(start, end):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    is_swapped = True

            if not is_swapped:
                break

            is_swapped = False
            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    is_swapped = True

            start = start + 1

        return numbers


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for i in range(10)]
    s = Solution()
    print(s.cock_tail(nums))
