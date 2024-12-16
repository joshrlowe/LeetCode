import pytest  # type: ignore
from palindrome_number import isPalindrome as is_palindrome


@pytest.mark.parametrize(
    "x, expected",
    [
        (121, True),
        (-121, False),
        (10, False),
        (7, True),
        (123454321, True),
        (123456789, False),
        (0, True),
    ],
)
def test_is_palindrome(x: int, expected: bool) -> None:
    result = is_palindrome(x)
    assert result == expected, f"x: {x}, expected: {expected}, result: {result}"
