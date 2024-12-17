import pytest  # type: ignore
from permutations_2 import permuteUnique as permute_unique
from typing import List


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([1], [[1]]),
        ([], [[]]),
        ([2, 2, 2], [[2, 2, 2]]),
    ],
)
def test_permute_unique(nums: List[int], expected: List[List[int]]) -> None:
    result = sorted(permute_unique(nums))
    expected.sort()
    assert result == expected, f"nums: {nums}, expected: {expected}, result: {result}"
