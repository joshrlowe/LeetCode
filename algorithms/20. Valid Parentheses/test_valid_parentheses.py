import pytest  # type: ignore
from valid_parentheses import isValid as is_valid


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("({[]})", True),
        ("(]", False),
        ("([)", False),
        ("", True),
        ("(((()))){{{{[]}}}}", True),
        ("(((())){{{{[]}}}", False),
        ("((()))", True),
        ("}}}}", False),
    ],
)
def test_is_valid(s: str, expected: bool) -> None:
    result = is_valid(s)
    assert result == expected, f"s: {s}, expected: {expected}, result: {result}"
