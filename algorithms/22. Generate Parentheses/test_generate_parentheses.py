import pytest  # type: ignore
from generate_parentheses import generateParenthesis as generate_parentheses
from typing import List


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, [""]),
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (
            4,
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
        ),
    ],
)
def test_generate_parentheses(n: int, expected: List[str]) -> None:
    result = sorted(generate_parentheses(n))
    expected = sorted(expected)
    assert result == expected, f"n: {n}, expected: {expected}, result: {result}"
