"""
Input : [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output : 14
"""

def get_max_sequesnce_sum(numbers: list[int]) -> int:
    result, current = 0, 0

    for num in numbers:
        current = max(num, current + num)
        result = max(result, current)
    return result

if __name__ == "__main__":
    numbers = [1, -2, 3, 6, -1, 2, 4, -5, 2]
    print(get_max_sequesnce_sum(numbers))