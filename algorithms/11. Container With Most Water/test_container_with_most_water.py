import pytest  # type: ignore
from container_with_most_water import maxArea as max_area
from typing import List


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([4, 4, 4, 4, 4, 4], 20),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25),
        ([1, 100], 1),
        ([10000, 1, 10000, 1, 10000], 40000),
        ([1, 3, 2, 5, 2, 4, 1], 12),
        ([1, 2, 3, 50, 3, 2, 1], 8),
    ],
)
def test_container_with_most_water(height: List[int], expected: int) -> None:
    result = max_area(height)
    assert (
        result == expected
    ), f"height: {height}, expected: {expected}, result: {result}"
