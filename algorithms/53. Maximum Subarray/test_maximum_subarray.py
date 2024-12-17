import pytest  # type: ignore
from maximum_subarray import maxSubArray as max_sub_array
from typing import List


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1, 2, 3, 4, 5], 15),
        ([-1, -2, -3, -4], -1),
        ([5], 5),
        ([1, 2, 3, -2, 5], 9),
        ([1000000, -1, 1000000, -1, 1000000], 2999998),
        ([2, -1, 2, -1, 2], 4),
    ],
)
def test_max_sub_array(nums: List[int], expected: int) -> None:
    result = max_sub_array(nums)
    assert result == expected, f"nums={nums}, expected={expected}, result={result}"
