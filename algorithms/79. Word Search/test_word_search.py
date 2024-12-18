import pytest  # type: ignore
from word_search import exist
from typing import List


@pytest.mark.parametrize(
    "board, word, expected",
    [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
        ([["A"]], "A", True),
        ([["A"]], "B", False),
        ([["A", "B"], ["C", "D"]], "ABCDAB", False),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
    ],
)
def test_exist(board: List[List[str]], word: str, expected: bool) -> None:
    result = exist(board, word)
    assert (
        result == expected
    ), f"board: {board}, word: {word}, expected: {expected}, result: {result}"
