import pytest  # type: ignore
from palindrome_permutation import canPermutePalindrome as can_permute_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("a", True),
        ("aa", True),
        ("aaa", True),
        ("aab", True),
        ("carerac", True),
        ("racecar", True),
        ("ab", False),
        ("abc", False),
        ("abcd", False),
        ("aabbcc", True),
        ("aabbccc", True),
        ("aabbccdd", True),
        ("aabbccdde", True),
        ("", True),
    ],
)
def test_can_permute_palindrome(s: str, expected: bool) -> None:
    result = can_permute_palindrome(s)
    assert result == expected, f"s: {s}, expected: {expected}, result: {result}"
