import pytest  # type: ignore
from typing import List
from pascal_triangle_2 import getRow as get_pascals_row


@pytest.mark.parametrize(
    "rowIndex, expected",
    [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
        (5, [1, 5, 10, 10, 5, 1]),
        (6, [1, 6, 15, 20, 15, 6, 1]),
        (7, [1, 7, 21, 35, 35, 21, 7, 1]),
        (8, [1, 8, 28, 56, 70, 56, 28, 8, 1]),
        (9, [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]),
        (10, [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]),
    ],
)
def test_get_pascals_row(rowIndex: int, expected: List[int]) -> None:
    result = get_pascals_row(rowIndex)
    assert (
        result == expected
    ), f"rowIndex: {rowIndex}, expected: {expected}, result: {result}"
