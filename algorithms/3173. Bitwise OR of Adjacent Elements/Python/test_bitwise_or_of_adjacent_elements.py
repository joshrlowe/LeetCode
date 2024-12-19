import pytest  # type: ignore
from bitwise_or_of_adjacent_elements import orArray as or_array
from typing import List


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [3, 3]),
        ([0, 0, 0], [0, 0]),
        ([1, 1, 1], [1, 1]),
        ([1, 2, 4, 8], [3, 6, 12]),
        ([7, 3, 1], [7, 3]),
        ([8, 4, 2, 1], [12, 6, 3]),
        ([5, 10, 15], [15, 15]),
        ([0, 1, 2, 3], [1, 3, 3]),
        ([1], []),
        ([1, 3, 7, 15], [3, 7, 15]),
    ],
)
def test_or_array(nums: List[int], expected: List[int]) -> None:
    result = or_array(nums)
    assert result == expected, f"nums: {nums}, expected: {expected}, result: {result}"
