import pytest  # type: ignore
from roman_to_integer import romanToInt as roman_to_integer


@pytest.mark.parametrize(
    "s, expected",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("M", 1000),
        ("VI", 6),
        ("XX", 20),
        ("XLIX", 49),
    ],
)
def test_roman_to_integer(s: str, expected: int) -> None:
    result = roman_to_integer(s)
    assert result == expected, f"s: {s}, expected {expected}, but got {result}"
