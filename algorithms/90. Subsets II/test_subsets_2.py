import pytest  # type: ignore
from subsets_2 import subsetsWithDup as subsets_with_dup
from typing import List


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], [[]]),
        ([1], [[], [1]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        ([1, 1], [[], [1], [1, 1]]),
        ([1, 2, 2], [[], [1], [2], [2, 2], [1, 2], [1, 2, 2]]),
        ([2, 1, 2], [[], [1], [2], [2, 2], [1, 2], [1, 2, 2]]),
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([1, 1, 1], [[], [1], [1, 1], [1, 1, 1]]),
        (
            [4, 4, 4, 1, 4],
            [
                [],
                [1],
                [4],
                [4, 4],
                [4, 4, 4],
                [4, 4, 4, 4],
                [1, 4],
                [1, 4, 4],
                [1, 4, 4, 4],
                [1, 4, 4, 4, 4],
            ],
        ),
        (
            [1, 2, 2, 3],
            [
                [],
                [1],
                [2],
                [2, 2],
                [3],
                [1, 2],
                [1, 2, 2],
                [1, 3],
                [2, 3],
                [2, 2, 3],
                [1, 2, 3],
                [1, 2, 2, 3],
            ],
        ),
    ],
)
def test_subsets_with_dup(nums: List[int], expected: List[List[int]]) -> None:
    result = subsets_with_dup(nums)
    result.sort()
    expected.sort()
    assert result == expected, f"nums: {nums}, expected: {expected}, result: {result}"
