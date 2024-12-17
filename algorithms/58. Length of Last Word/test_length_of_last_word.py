import pytest  # type: ignore
from length_of_last_word import lengthOfLastWord as length_of_last_word


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello World", 5),
        ("Python programming", 11),
        ("The quick brown fox", 3),
        ("Hello World   ", 5),
        ("   trailing spaces   ", 6),
        ("Word", 4),
        ("SingleWord   ", 10),
        ("   ", 0),
        ("", 0),
        ("Hello     World", 5),
        ("   multiple   spaces between   words   ", 5),
        ("a", 1),
        ("a " * 10000 + "word", 4),
        ("123 456", 3),
        ("!@#$%^&*() last_word", 9),
        ("word_with_underscores", 21),
        ("1234567890", 10),
    ],
)
def test_length_of_last_word(s: str, expected: int) -> None:
    result = length_of_last_word(s)
    assert result == expected, f"s: {s}, expected: {expected}, result: {result}"
