import pytest  # type: ignore
from combination_sum_3 import combinationSum3 as combination_sum_3
from typing import List


@pytest.mark.parametrize(
    "k, n, expected",
    [
        (3, 7, [[1, 2, 4]]),
        (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
        (2, 18, []),
        (2, 5, [[1, 4], [2, 3]]),
        (1, 1, [[1]]),
        (1, 9, [[9]]),
        (
            3,
            15,
            [
                [1, 5, 9],
                [1, 6, 8],
                [2, 4, 9],
                [2, 5, 8],
                [2, 6, 7],
                [3, 4, 8],
                [3, 5, 7],
                [4, 5, 6],
            ],
        ),
        (4, 1, []),
        (3, 2, []),
        (2, 6, [[1, 5], [2, 4]]),
    ],
)
def test_combination_sum_3(k: int, n: int, expected: List[List[int]]) -> None:
    result = combination_sum_3(k, n)
    assert sorted(result) == sorted(
        expected
    ), f"k: {k}, n: {n}, expected: {expected}, result: {result}"
