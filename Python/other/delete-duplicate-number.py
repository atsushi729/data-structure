"""
Input : [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
Output :[1, 3, 5, 7, 10, 12, 15]
Condition : Not allow to use built-in function like set() dict.fromkeys()
"""


def delete_duplicate_numbers(numbers: list[int]) -> list[int]:
    delete_duplicate_num = []

    for num in numbers:
        if num not in delete_duplicate_num:
            delete_duplicate_num.append(num)

    return delete_duplicate_num


if __name__ == "__main__":
    numbers = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
    print(delete_duplicate_numbers(numbers))
