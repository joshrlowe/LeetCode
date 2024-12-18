import pytest  # type: ignore
from sqrtx import mySqrt as my_sqrt


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (16, 4),
        (25, 5),
        (26, 5),
        (100, 10),
        (101, 10),
        (2147395599, 46339),
        (2, 1),
        (3, 1),
        (15, 3),
        (49, 7),
        (50, 7),
        (999999999, 31622),
        (2147483647, 46340),
        (2147395600, 46340),
        (100000000, 10000),
    ],
)
def test_my_sqrt(x: int, expected: int) -> None:
    result = my_sqrt(x)
    assert result == expected, f"x: {x}, expected: {expected}, result: {result}"
