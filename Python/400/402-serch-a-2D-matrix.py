class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        for first in matrix:
            for element in first:
                if element > target:
                    break

                if element == target:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    ans = s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    print(ans)

