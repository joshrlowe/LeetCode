import pytest  # type: ignore
from power_of_two import isPowerOfTwo as is_power_of_two


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (2, True),
        (4, True),
        (8, True),
        (16, True),
        (32, True),
        (64, True),
        (128, True),
        (256, True),
        (512, True),
        (1024, True),
        (2048, True),
        (4096, True),
        (8192, True),
        (16384, True),
        (32768, True),
        (65536, True),
        (3, False),
        (5, False),
        (6, False),
        (7, False),
        (9, False),
        (15, False),
        (100, False),
        (-1, False),
        (0, False),
        (-8, False),
    ],
)
def test_is_power_of_two(n: int, expected: bool) -> None:
    result = is_power_of_two(n)
    assert result == expected, f"n: {n}, expected: {expected}, result: {result}"
