import pytest  # type: ignore
from longest_substring_without_repeating_characters import (
    lengthOfLongestSubstring as length_of_longest_substring,
)


@pytest.mark.parametrize(
    ["s", "expected"],
    [
        ("abcabcbb", 3),
        ("abcdef", 6),
        ("aaaaaa", 1),
        ("", 0),
        ("a!@#a!@#", 4),
        ("a b c a b c", 3),
        ("aAaA", 2),
        ("abcdefghijklmnopqrstuvwxyz", 26),
        ("a1b2c3d4", 8),
        ("abcabcabcabcabcabcabcabcabcabc", 3),
    ],
)
def test_length_of_longest_substring(s, expected):
    result = length_of_longest_substring(s)
    assert result == expected, f"s: {s}, expected: {expected}, result: {result}"
