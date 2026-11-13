import unittest


#################### Solution ####################
class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        reasonable_row = []
        left, right = 0, len(matrix[0]) - 1

        # find reasonable row
        for row in matrix:
            if row[0] <= target <= row[-1]:
                reasonable_row = row
                break

        # if reasonable row is empty, return False
        if len(reasonable_row) == 0:
            return False

        # find target from row
        while left <= right:
            middle = (left + right) // 2
            if reasonable_row[middle] == target:
                return True
            elif reasonable_row[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False

    def search_matrix_v2(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def search_matrix_v3(self, matrix: list[list[int]], target: int) -> bool:
        flatted_matrix = [element for row in matrix for element in row]

        left, right = 0, len(flatted_matrix) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if flatted_matrix[mid] == target:
                return True
            elif flatted_matrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def search_matrix_v4(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return target in row
        return False

    def search_matrix_v5(self, matrix: list[list[int]], target: int) -> bool:
        target_row = 0

        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                target_row = i
                break

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2

            if target == matrix[target_row][mid]:
                return True
            elif target < matrix[target_row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def search_matrix_v6(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            current_val = matrix[row][col]

            if current_val == target:
                return True
            elif current_val > target:
                col -= 1
            else:
                row += 1
        return False


#################### Test Case ####################
class TestSearchMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

        cls.methods = [
            cls.s.search_matrix,
            cls.s.search_matrix_v2,
            cls.s.search_matrix_v3,
            cls.s.search_matrix_v4,
            cls.s.search_matrix_v5,
            cls.s.search_matrix_v6,
        ]

        cls.test_cases = [
            # Basic cases
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),

            # Single element
            ([[1]], 1, True),
            ([[1]], 2, False),
            ([[1]], 0, False),

            # Single row
            ([[1, 3, 5, 7, 9]], 5, True),
            ([[1, 3, 5, 7, 9]], 6, False),

            # Single column
            ([[1], [3], [5], [7], [9]], 5, True),
            ([[1], [3], [5], [7], [9]], 6, False),

            # Boundary cases
            ([[1, 3, 5], [7, 9, 11]], 1, True),
            ([[1, 3, 5], [7, 9, 11]], 11, True),
            ([[1, 3, 5], [7, 9, 11]], 0, False),
            ([[1, 3, 5], [7, 9, 11]], 12, False),

            # Negative numbers
            ([[-10, -5, -1], [0, 3, 7], [10, 15, 20]], -5, True),
            ([[-10, -5, -1], [0, 3, 7], [10, 15, 20]], -3, False),

            # Target between rows
            ([[1, 2, 3], [10, 11, 12]], 5, False),

            # Large values
            ([[1, 100, 1000], [2000, 3000, 4000]], 3000, True),
            ([[1, 100, 1000], [2000, 3000, 4000]], 1500, False),
        ]

    def test_search_matrix(self):
        for method in self.methods:
            for matrix, target, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        matrix=matrix,
                        target=target,
                        expected=expected,
                ):
                    self.assertEqual(
                        method(matrix, target),
                        expected,
                    )
