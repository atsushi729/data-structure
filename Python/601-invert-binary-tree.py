import math


def invertTree(root: list):
    tmp = []

    while root:
        target = math.floor(math.log2(len(root) + 1))
        target_array = math.floor(root[-target, -1])
        revers_array = reversed(target_array)
        tmp.insert(0, revers_array)
        del root[-target, -1]

    return tmp


root = [int(i) for i in input().split()]
print(invertTree(root))
