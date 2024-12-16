import pytest  # type: ignore
from median_of_two_sorted_arrays import (
    findMedianSortedArrays as find_median_sorted_arrays,
)


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([1], [2], 1.5),
        ([1, 3, 8], [7, 9, 10, 11], 8.0),
        ([1, 2, 3], [1, 2, 3], 2.0),
        ([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10], 3.0),
        ([1, 2, 2], [2, 3, 4], 2.0),
    ],
)
def test_find_median_sorted_arrays(nums1, nums2, expected):
    result = find_median_sorted_arrays(nums1, nums2)
    assert (
        result == expected
    ), f"nums1: {nums1}, nums2: {nums2}, expected: {expected}, result: {result}"
