import pytest  # type: ignore
from find_minimum_operations_to_make_all_elements_divisible_by_three import (
    minimumOperations as minimum_operations,
)
from typing import List


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0], 0),
        ([1], 1),
        ([3], 0),
        ([3, 6, 9], 0),
        ([0, 3, 6], 0),
        ([1, 2, 4], 3),
        ([1, 3, 6, 9, 2], 2),
        ([2, 5, 8, 11], 4),
        ([7, 14, 21, 28], 3),
    ],
)
def test_minimum_operations(nums: List[int], expected: int) -> None:
    result = minimum_operations(nums)
    assert result == expected, f"nums: {nums}, expected: {expected}, result: {result}"
