from typing import List


class Solution:
    def binary_search(self, numbers: List[int], target: int) -> int:
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2

            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                left += mid + 1
            else:
                right = mid - 1
        return -1


# Time Complexity: O(log n)
# if __name__ == "__main__":
#     s = Solution()
# import random
# numbers = [random.randint(0, 100) for _ in range(10)]
# numbers = [2, 3, 4, 10, 40]
# print(s.binary_search(numbers, 10))

"""
Recursive version
"""


class Recursive:
    def recursive_binary_search(self, numbers: List[int], left: int, right: int, target: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            return self.recursive_binary_search(numbers, mid + 1, right, target)
        else:
            return self.recursive_binary_search(numbers, left, mid - 1, target)


# Time Complexity: O(log n)
# if __name__ == "__main__":
#     s = Recursive()
#     numbers = [2, 3, 4, 10, 40]
#     print(s.recursive_binary_search(numbers, 0, len(numbers), 40))

"""
Insert binary tree
"""


class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def minValue(node: Node) -> Node:
    current = node
    while current.left is not None:
        current = current.left
    return current


def remove(node: Node, value: int) -> Node:
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.rigth is None:
            return node.left

        tmp = minValue(node.right)
        node.value = tmp.value
        node.right = remove(node.right, tmp.value)
    return node


if __name__ == "__main__":
    root = None
    root = insert(root, 3)
    root = insert(root, 8)
    root = insert(root, 1)
    root = remove(root, 1)
