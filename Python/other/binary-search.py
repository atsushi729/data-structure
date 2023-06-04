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
if __name__ == "__main__":
    s = Recursive()
    numbers = [2, 3, 4, 10, 40]
    print(s.recursive_binary_search(numbers, 0, len(numbers), 40))
