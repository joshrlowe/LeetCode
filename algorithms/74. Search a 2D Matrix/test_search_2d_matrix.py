import pytest  # type: ignore
from Python.search_2d_matrix_solution_1 import searchMatrix as search_matrix_1
from Python.search_2d_matrix_solution_2 import searchMatrix as search_matrix_2
from typing import List


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        ([[1]], 1, True),
        ([[1]], 2, False),
        ([[1, 3, 5, 7]], 3, True),
        ([[1, 3, 5, 7]], 6, False),
        ([[1], [3], [5], [7]], 5, True),
        ([[1], [3], [5], [7]], 4, False),
        ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9, True),
        ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 4, False),
        ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 15, True),
        ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 17, True),
        ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 18, False),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8, True),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10, False),
        ([[1, 3, 5], [10, 11, 16], [23, 30, 34]], 30, True),
        ([[1, 3, 5], [10, 11, 16], [23, 30, 34]], 35, False),
        ([[1, 3, 5], [10, 11, 16], [23, 30, 34]], 16, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 8, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1, True),
    ],
)
def test_search_matrix(matrix: List[List[int]], target: int, expected: bool) -> None:
    result_1 = search_matrix_1(matrix, target)
    assert (
        result_1 == expected
    ), f"matrix: {matrix}, target: {target}, expected: {expected}, result: {result_1}"

    result_2 = search_matrix_1(matrix, target)
    assert (
        result_2 == expected
    ), f"matrix: {matrix}, target: {target}, expected: {expected}, result: {result_2}"
