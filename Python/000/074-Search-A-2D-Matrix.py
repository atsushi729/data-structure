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


#################### Test Case ####################
class TestSearchMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
            ([[1]], 1, True),
            ([[1]], 2, False),
        ]

    def test_search_matrix(self):
        for matrix, target, expected in self.test_cases:
            with self.subTest(matrix=matrix, target=target, expected=expected):
                self.assertEqual(self.s.search_matrix(matrix, target), expected)

    def test_model_search_matrix(self):
        for matrix, target, expected in self.test_cases:
            with self.subTest(matrix=matrix, target=target, expected=expected):
                self.assertEqual(self.s.search_matrix_v2(matrix, target), expected)

    def test_model_search_matrix_v3(self):
        for matrix, target, expected in self.test_cases:
            with self.subTest(matrix=matrix, target=target, expected=expected):
                self.assertEqual(self.s.search_matrix_v3(matrix, target), expected)

    def test_model_search_matrix_v4(self):
        for matrix, target, expected in self.test_cases:
            with self.subTest(matrix=matrix, target=target, expected=expected):
                self.assertEqual(self.s.search_matrix_v4(matrix, target), expected)