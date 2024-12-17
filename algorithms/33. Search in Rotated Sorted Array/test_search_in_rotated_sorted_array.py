import pytest  # type: ignore
from Python.search_in_rotated_sorted_array_solution_1 import search as search_1
from Python.search_in_rotated_sorted_array_solution_2 import search as search_2
from typing import List


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1, 2, 3, 4, 5, 6, 7], 5, 4),
        ([1, 2, 3, 4, 5, 6, 7], 8, -1),
        ([1], 1, 0),
        ([1], 0, -1),
        ([6, 7, 8, 9, 1, 2, 3, 4, 5], 9, 3),
        ([2, 3, 4, 5, 6, 7, 1], 1, 6),
    ],
)
def test_search(nums: List[int], target: int, expected: int) -> None:
    result_1 = search_1(nums, target)
    assert result_1 == search_1(
        nums, target
    ), f"nums: {nums}, target: {target}, expected_1: {expected}, result_1: {result_1}"

    result_2 = search_2(nums, target)
    assert result_2 == search_2(
        nums, target
    ), f"nums: {nums}, target: {target}, expected_2: {expected}, result_2: {result_2}"
