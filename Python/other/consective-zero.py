"""
version 1
"""
# def solution(n: int) -> int:
#     binary_box = []
#     result = []
#     current_max = 0
#
#     while n > 0:
#         tmp = n % 2
#         binary_box.append(tmp)
#         n = (n - tmp) // 2
#
#     for i in binary_box[::-1]:
#         if i == 1 and 1 not in result:
#             result.append(1)
#
#         elif i == 1 and 1 in result:
#             current_max = result.count(0)
#             result = []
#
#         elif i == 0 and 1 in result:
#             result.append(0)
#
#     return current_max

"""
version 2
"""


def solution(N):
    binary = bin(N)[2:]  # Convert N to binary representation
    max_gap = 0
    current_gap = 0
    counting = False

    for digit in binary:
        if digit == '1':
            if counting:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                counting = True
        elif counting:
            current_gap += 1

    return max_gap


if __name__ == "__main__":
    print(solution(1041))
