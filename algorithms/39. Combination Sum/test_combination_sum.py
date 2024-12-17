import pytest  # type: ignore
from combination_sum import combinationSum as combination_sum
from typing import List


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 4, 6, 8], 5, []),
        ([7], 7, [[7]]),
        ([3], 9, [[3, 3, 3]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([], 7, []),
        ([1], 2, [[1, 1]]),
    ],
)
def test_combination_sum(candidates: List[int], target: int, expected: List[List[int]]):
    result = combination_sum(candidates, target)
    assert (
        result == expected
    ), f"candidates: {candidates}, target: {target}, expected: {expected}, result: {result}"
