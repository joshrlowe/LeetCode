import pytest  # type: ignore
from three_sum import threeSum as three_sum
from typing import List


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([1, 2, -2, -1], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        (
            [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
            [
                [-4, 0, 4],
                [-4, 1, 3],
                [-3, -1, 4],
                [-3, 0, 3],
                [-3, 1, 2],
                [-2, -1, 3],
                [-2, 0, 2],
                [-1, -1, 2],
                [-1, 0, 1],
            ],
        ),
        ([], []),
        ([1, -1, -1, 0], [[-1, 0, 1]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-1, 2, -3, 4, -2, 1], [[-3, -1, 4], [-3, 1, 2]]),
    ],
)
def test_three_sum(nums: List[int], expected: List[List[int]]) -> None:
    result = three_sum(nums)
    assert result == expected, f"nums: {nums}, expected: {expected}, result: {result}"
