"""
## Input data type:
type : int
range: -10 <= matrix[i][j] <= 10

## Note:
(come back later when write unit test!)

## Ignore case
1. matrix = Null (should have some value.)

## Design how to solve this problem
### Brute force way 
1. Nested for loop.
2. Switch index position(i and j)
Pro:
 - easy to implement
 - easy to test
Con:
 - Not efficient (O(n^2))

### Another solution??

"""
import unittest


#################### Solution ####################
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    answer = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            answer[j][i] = matrix[i][j]

    return answer


#################### Test Case ####################
class TestTranspose(unittest.TestCase):
    def test_transpose(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
