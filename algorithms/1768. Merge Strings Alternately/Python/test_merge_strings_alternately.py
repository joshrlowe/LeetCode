import pytest  # type: ignore
from merge_strings_alternately import mergeAlternately as merge_alternately


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "xyz", "xyz"),
        ("hello", "", "hello"),
        ("a", "b", "ab"),
        ("", "", ""),
        ("short", "longer", "slhoonrgter"),
    ],
)
def test_merge_alternately(word1, word2, expected):
    result = merge_alternately(word1, word2)
    assert (
        result == expected
    ), f"word1: {word1}, word2: {word2}, expected: {expected}, result: {result}"
