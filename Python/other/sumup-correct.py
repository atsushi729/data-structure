def remove_zero(numbers: list[int]) -> int:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: list[int]) -> int:
    result = 0

    for i, num in enumerate(reversed(numbers)):
        result += num * (10 ** i)
    return result


def list_to_int_plus_one(numbers: list[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1

    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        numbers[i] = 0
        numbers[i - 1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)


if __name__ == "__main__":
    numbers = [0, 2, 9]
    print(list_to_int_plus_one(numbers))
