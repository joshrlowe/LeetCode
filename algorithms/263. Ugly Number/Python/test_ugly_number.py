import pytest  # type: ignore
from ugly_number import isUgly as is_ugly


@pytest.mark.parametrize(
    "n, expected",
    [
        # Positive Ugly Numbers
        (1, True),
        (2, True),
        (3, True),
        (5, True),
        (6, True),
        (8, True),
        (10, True),
        (12, True),
        (15, True),
        (30, True),
        (60, True),
        # Non-Ugly Numbers
        (14, False),
        (25, True),
        (21, False),
        (49, False),
        (13, False),
        (7, False),
        (22, False),
        (9, True),
        # Edge Cases
        (0, False),
        (-1, False),
        (-6, False),
        (2147483647, False),
        (2**31, True),
        (2**3 * 3**2 * 5**1, True),
        (2**3 * 3**2 * 7, False),
    ],
)
def test_is_ugly(n: int, expected: bool) -> None:
    result = is_ugly(n)
    assert result == expected, f"n: {n}, expected: {expected}, result: {result}"
