import pytest  # type: ignore
from merge_sorted_array import merge
from typing import List

@pytest.mark.parametrize("nums1, m, nums2, n, expected", [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([2, 0], 1, [1], 1, [1, 2]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ([1, 2, 4, 5, 6, 0], 5, [3], 1, [1, 2, 3, 4, 5, 6]),
    ([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 0, 0, 0, 0], 3, [2, 2, 3, 4], 4, [1, 2, 2, 2, 3, 3, 4]),
    ([1, 0, 0], 1, [2, 3], 2, [1, 2, 3]),
    ([1, 2, 3, 0, 0, 0], 3, [0, 0, 0], 3, [0, 0, 0, 1, 2, 3]),
    ([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3, 4, 0, 0, 0, 0], 4, [2, 4, 6, 8], 4, [1, 2, 2, 3, 4, 4, 6, 8]),
])
def test_merge(nums1: List[int], m: int, nums2: List[int], n: int, expected: List[int]) -> None:
    merge(nums1, m, nums2, n)
    assert nums1 == expected, f"nums1: {nums1}, expected: {expected}"
