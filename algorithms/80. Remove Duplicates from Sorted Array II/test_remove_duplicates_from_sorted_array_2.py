import pytest  # type: ignore
from remove_duplicates_from_sorted_array_2 import removeDuplicates as remove_duplicates
from typing import List


@pytest.mark.parametrize(
    "nums, expected_nums, expected_k",
    [
        ([], [], 0),
        ([1], [1], 1),
        ([1, 1, 1], [1, 1], 2),
        ([1, 1, 2], [1, 1, 2], 3),
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3], 5),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3], 7),
        ([1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3], 6),
        ([1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 3], 5),
        ([1, 1, 1, 1, 1, 1], [1, 1], 2),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5),
        ([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5], [1, 1, 2, 2, 3, 3, 4, 4, 5], 9),
        ([1, 2, 2, 2, 3, 3, 3, 3], [1, 2, 2, 3, 3], 5),
    ],
)
def test_remove_duplicates(
    nums: List[int], expected_nums: List[int], expected_k: int
) -> None:
    k = remove_duplicates(nums)
    assert k == expected_k, f"nums: {nums}, expected_k: {expected_k}, k: {k}"
    assert (
        nums[:k] == expected_nums[:k]
    ), f"nums: {nums[:k]}, expected_nums: {expected_nums[:k]}"
