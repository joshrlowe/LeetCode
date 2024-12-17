import pytest  # type: ignore
from remove_duplicates_from_sorted_array import removeDuplicates as remove_duplicates
from typing import List


@pytest.mark.parametrize(
    "nums, expected_k, expected_nums",
    [
        ([], 0, []),
        ([1], 1, [1]),
        ([1, 1, 2], 2, [1, 2]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
        ([2, 2, 2, 2, 2], 1, [2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ],
)
def test_remove_duplicates(
    nums: List[int], expected_k: int, expected_nums: List[int]
) -> None:
    starting_nums = nums[:]
    result = remove_duplicates(nums)
    assert (
        result == expected_k
    ), f"nums: {starting_nums}, expected_k: {expected_k}, result_k: {result}"
    assert (
        nums[:result] == expected_nums
    ), f"nums: {starting_nums}, expected_nums: {expected_nums}, result_nums: {nums}"
