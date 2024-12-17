import pytest  # type: ignore
from trapping_rain_water import trap
from typing import List


@pytest.mark.parametrize(
    "height, expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([1, 1, 1, 1, 1], 0),
        ([5, 4, 3, 2, 1], 0),
        ([1, 2, 3, 4, 5], 0),
        ([3, 0, 2, 0, 4], 7),
        ([0], 0),
        ([1, 0], 0),
        ([1000, 100, 1000, 100, 1000], 1800),
    ],
)
def test_trap(height: List[int], expected: int) -> None:
    result = trap(height)
    assert result == expected, f"height: {height}, expected {expected}, result {result}"
