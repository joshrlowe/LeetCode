import pytest  # type: ignore
from n_queens_2 import totalNQueens as total_n_queens
from typing import List


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 2),
        (5, 10),
        (6, 4),
        (7, 40),
        (8, 92),
        (9, 352),
        (10, 724),
        (11, 2680),
        (12, 14200),
    ],
)
def test_total_n_queens(n: int, expected: int) -> None:
    result = total_n_queens(n)
    assert result == expected, f"n: {n}, expected: {expected}, result: {result}"
