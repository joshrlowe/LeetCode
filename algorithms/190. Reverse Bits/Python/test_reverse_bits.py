import pytest  # type: ignore
from reverse_bits import reverseBits as reverse_bits


@pytest.mark.parametrize(
    "n, expected",
    [
        ("00000000000000000000000000000101", 2684354560),
        ("00000000000000000000000000000001", 2147483648),
        ("00000000000000000000000000000111", 3758096384),
        ("00000000000000000000000000010101", 2818572288),
        ("00000000000000001000000000000000", 65536),
        ("00000000000000000000000000000000", 0),
        ("00000000000000000000000000000110", 1610612736),
        ("11111111111111111111111111111101", 3221225471),
        ("00000010100101000001111010011100", 964176192),
    ],
)
def test_reverse_bits(n: str, expected: int) -> None:
    result = reverse_bits(int(n, 2))
    assert result == expected, f"n: {n}, expected: {expected}, result: {result}"
