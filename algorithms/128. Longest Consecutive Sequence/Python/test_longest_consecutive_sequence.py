import pytest  # type: ignore
from typing import List
from longest_consecutive_sequence import longestConsecutive as longest_consecutive


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], 0),
        ([1], 1),
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, -1, 1, 2, 3], 5),
        ([1, 2, 0, 1], 3),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -2, 6], 7),
        ([10, 5, 12, 3, 55, 6, 4], 4),
        ([5, 5, 5, 5], 1),
        ([-10, -9, -8, -7], 4),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
    ],
)
def test_longest_consecutive(nums: List[int], expected: int) -> None:
    result = longest_consecutive(nums)
    assert result == expected, f"nums: {nums}, expected: {expected}, result: {result}"
