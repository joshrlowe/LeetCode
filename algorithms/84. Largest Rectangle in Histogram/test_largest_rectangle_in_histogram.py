import pytest  # type: ignore
from largest_rectangle_in_histogram import largestRectangleArea as largest_rectangle_area
from typing import List

@pytest.mark.parametrize("heights, expected", [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([1, 1, 1, 1, 1], 5),
    ([1], 1),
    ([0], 0),
    ([2, 1, 2], 3),
    ([3, 1, 3, 2, 2], 6),
    ([5, 4, 1, 2], 8),
    ([1, 2, 3, 4, 5], 9),
    ([5, 4, 3, 2, 1], 9),
    ([1, 2, 3, 2, 1], 6),
    ([1, 2, 3, 4, 3, 2, 1], 10),
    ([2, 2, 2, 2, 2], 10),
    ([0, 0, 0, 0], 0),
    ([6, 2, 5, 4, 5, 1, 6], 12),
    ([2, 1, 5, 6, 2, 3, 1], 10),
    ([1, 1, 1, 1, 2, 2, 2], 7),
    ([1, 8, 8, 1, 8], 16),
    ([10000], 10000),
    ([1, 10000, 1], 10000),
])
def test_largest_rectangle_area(heights: List[int], expected: int) -> None:
    result = largest_rectangle_area(heights)
    assert result == expected, f"heights: {heights}, expected: {expected}, result: {result}"
