import pytest  # type: ignore
from combination_sum_ii import combinationSum2 as combination_sum_2
from typing import List


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 4, 6], 1, []),
        ([3], 3, [[3]]),
        ([], 5, []),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2, [[1, 1]]),
        ([1, 2, 3], 10, []),
    ],
)
def test_combination_sum_2(
    candidates: List[int], target: int, expected: List[List[int]]
) -> None:
    result = combination_sum_2(candidates, target)
    assert (
        result == expected
    ), f"candidates: {candidates}, target: {target}, expected: {expected}, result: {result}"
