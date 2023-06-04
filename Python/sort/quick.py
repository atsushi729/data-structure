from typing import List


def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]

    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1

            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
    return i + 1


def quick_sort(numbers: List[int], low: int, high: int) -> List[int]:
    if low < high:
        pivot = partition(numbers, low, high)

        ## sort left hand side of pivot
        quick_sort(numbers, low, pivot - 1)

        ## sort right hand side of pivot
        quick_sort(numbers, pivot + 1, high)
    return numbers


if __name__ == "__main__":
    numbers = [2, 6, 4, 7, 12, 3, 5]
    print(quick_sort(numbers, 0, len(numbers) - 1))
