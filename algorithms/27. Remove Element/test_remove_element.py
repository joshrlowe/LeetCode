import pytest  # type: ignore
from remove_element import removeElement as remove_element
from typing import List


@pytest.mark.parametrize(
    "nums, val, expected",
    [
        ([3, 2, 2, 3], 3, 2),
        ([1, 2, 3, 4], 5, 4),
        ([4, 4, 4, 4], 4, 0),
        ([], 1, 0),
        ([1], 1, 0),
        ([1], 2, 1),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
    ],
)
def test_remove_element(nums: List[int], val: int, expected: int) -> None:
    result = remove_element(nums, val)
    assert (
        result == expected
    ), f"nums: {nums}, val: {val}, expected: {expected}, result: {result}"
