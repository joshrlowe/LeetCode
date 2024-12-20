import pytest  # type: ignore
from number_of_1_bits import hammingWeight as hamming_weight


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 1),
        (7, 3),
        (8, 1),
        (15, 4),
        (31, 5),
        (2147483648, 1),
        (4294967295, 32),
    ],
)
def test_hamming_weight(n: int, expected: int) -> None:
    result = hamming_weight(n)
    assert result == expected, f"n: {n}, expected: {expected}, result: {result}"
