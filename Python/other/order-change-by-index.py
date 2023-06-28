"""
elements : ['y', 'k', 't', 'o', 'o']
numbers : [2, 4, 1, 0, 3]
output : tokyo
"""

def order_change_by_index(elements: list[str], numbers: list[int]) -> str:
    tmp = []

    for num in numbers:
        tmp.append(elements[num])

    result = ''.join(tmp)
    return result


if __name__ == "__main__":
    elements = ['y', 'k', 't', 'o', 'o']
    numbers = [2, 4, 1, 0, 3]
    print(order_change_by_index(elements, numbers))