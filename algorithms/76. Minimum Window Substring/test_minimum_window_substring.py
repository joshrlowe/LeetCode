import pytest  # type: ignore
from minimum_window_substring import minWindow as min_window


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "a", "a"),
        ("ab", "b", "b"),
        ("abc", "cba", "abc"),
        ("abc", "d", ""),
        ("aa", "aa", "aa"),
        ("aaab", "ab", "ab"),
        ("aabbcc", "abc", "abbc"),
        ("ADOBECODEBANC", "AABC", "ADOBECODEBA"),
        ("ADOBECODEBANC", "XYZ", ""),
        ("ABCD", "BC", "BC"),
        ("a" * 1000 + "b", "ab", "ab"),
        ("abcdebdde", "bde", "deb"),
        ("abcdebddebca", "bde", "deb"),
        ("aaflslflsldkalskaaa", "aaa", "aaa"),
    ],
)
def test_min_window(s: str, t: str, expected: str) -> None:
    result = min_window(s, t)
    assert result == expected, f"s: {s}, t: {t}, expected: {expected}, result: {result}"
