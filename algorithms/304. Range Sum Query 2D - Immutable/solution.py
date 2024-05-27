from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.sumMat = []
            return

        n, m = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (m + 1) for _ in range(n + 1)]

        for r in range(n):
            for c in range(m):
                self.sumMat[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.sumMat[r][c + 1]
                    + self.sumMat[r + 1][c]
                    - self.sumMat[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]

        return bottomRight - above - left + topLeft


def test_NumMatrix():
    # Test case 1: General case
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    numMatrix = NumMatrix(matrix)
    assert numMatrix.sumRegion(2, 1, 4, 3) == 8, "Test case 1 failed"
    assert numMatrix.sumRegion(1, 1, 2, 2) == 11, "Test case 1 failed"
    assert numMatrix.sumRegion(1, 2, 2, 4) == 12, "Test case 1 failed"

    # Test case 2: Single row matrix
    matrix = [[1, 2, 3, 4, 5]]
    numMatrix = NumMatrix(matrix)
    assert numMatrix.sumRegion(0, 0, 0, 4) == 15, "Test case 2 failed"
    assert numMatrix.sumRegion(0, 1, 0, 3) == 9, "Test case 2 failed"
    assert numMatrix.sumRegion(0, 2, 0, 2) == 3, "Test case 2 failed"

    # Test case 3: Single column matrix
    matrix = [[1], [2], [3], [4], [5]]
    numMatrix = NumMatrix(matrix)
    assert numMatrix.sumRegion(0, 0, 4, 0) == 15, "Test case 3 failed"
    assert numMatrix.sumRegion(1, 0, 3, 0) == 9, "Test case 3 failed"
    assert numMatrix.sumRegion(2, 0, 2, 0) == 3, "Test case 3 failed"

    # Test case 4: Matrix with negative values
    matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    numMatrix = NumMatrix(matrix)
    assert numMatrix.sumRegion(0, 0, 2, 2) == -45, "Test case 4 failed"
    assert numMatrix.sumRegion(1, 1, 2, 2) == -28, "Test case 4 failed"
    assert numMatrix.sumRegion(0, 0, 1, 1) == -12, "Test case 4 failed"

    # Test case 5: Matrix with zeroes
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    numMatrix = NumMatrix(matrix)
    assert numMatrix.sumRegion(0, 0, 2, 2) == 0, "Test case 5 failed"
    assert numMatrix.sumRegion(1, 1, 2, 2) == 0, "Test case 5 failed"
    assert numMatrix.sumRegion(0, 0, 1, 1) == 0, "Test case 5 failed"

    print("All test cases passed.")


test_NumMatrix()
