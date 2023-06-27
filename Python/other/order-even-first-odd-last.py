def order_even_first_odd_last(numbers: list[int]) -> list[int]:
    even_list, odd_list = [], []

    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    numbers[:] = even_list + odd_list
    return numbers

def v2(numbers: list[int]) -> list[int]:
    i, j = 0, len(numbers) - 1

    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= i
    return numbers

if __name__ == "__main__":
    numbers = [0, 1, 4, 6, 3, 2, 5, 6, 3, 6, 7, 9, 4, ]
    print(v2(numbers))
