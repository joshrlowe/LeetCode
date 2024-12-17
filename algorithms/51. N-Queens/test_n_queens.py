import pytest  # type: ignore
from n_queens import solveNQueens as solve_n_queens
from typing import List


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [["Q"]]),
        (2, []),
        (3, []),
        (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
        (
            5,
            [
                ["Q....", "..Q..", "....Q", ".Q...", "...Q."],
                ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
                [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
                [".Q...", "....Q", "..Q..", "Q....", "...Q."],
                ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
                ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
                ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
                ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
                ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
                ["....Q", "..Q..", "Q....", "...Q.", ".Q..."],
            ],
        ),
    ],
)
def test_solve_n_queens(n: int, expected: List[List[str]]) -> None:
    result = sorted(solve_n_queens(n))
    expected.sort()
    assert result == expected, f"n: {n}, expected: {expected}, result: {result}"
