def search(nums: list[int], target: int):
    numbers = sorted(nums)

    middle = round(len(numbers) / 2)
    middle_value = numbers[middle]

    if target == middle_value:
        return middle
    elif target > middle_value:
        numbers[0:middle] = []
    else:
        numbers[middle:-1] = []

    return numbers


nums = [int(x) for x in input().split()]
target = int(input())
print(search(nums, target))
