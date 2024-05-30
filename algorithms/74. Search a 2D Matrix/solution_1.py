from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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


def test_searchMatrix():
    solution = Solution()

    # Test Case 1: Target is in the matrix
    print("Test 1: Target is in the matrix")
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    expected = True
    result = solution.searchMatrix(matrix, target)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Target is not in the matrix
    print("Test 2: Target is not in the matrix")
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    expected = False
    result = solution.searchMatrix(matrix, target)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Single element matrix with target
    print("Test 3: Single element matrix with target")
    matrix = [[5]]
    target = 5
    expected = True
    result = solution.searchMatrix(matrix, target)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Single element matrix without target
    print("Test 4: Single element matrix without target")
    matrix = [[5]]
    target = 3
    expected = False
    result = solution.searchMatrix(matrix, target)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Large matrix with target
    print("Test 5: Large matrix with target")
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 5
    expected = True
    result = solution.searchMatrix(matrix, target)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Matrix with multiple identical rows
    print("Test 6: Matrix with multiple identical rows")
    matrix = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
    target = 2
    expected = True
    result = solution.searchMatrix(matrix, target)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")


if __name__ == "__main__":
    test_searchMatrix()
