from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m * n - 1

    while l <= r:
        mid = (l + r) // 2
        if target > matrix[mid // n][mid % n]:
            l = mid + 1
        elif target < matrix[mid // n][mid % n]:
            r = mid - 1
        else:
            return True
    return False
