import pytest  # type: ignore
from excel_sheet_column_number import titleToNumber as title_to_number


@pytest.mark.parametrize(
    "columnTitle, expected",
    [
        ("A", 1),
        ("B", 2),
        ("Z", 26),
        ("AA", 27),
        ("AB", 28),
        ("AZ", 52),
        ("BA", 53),
        ("ZZ", 702),
        ("AAA", 703),
        ("ABC", 731),
        ("XYZ", 16900),
    ],
)
def test_title_to_number(columnTitle: str, expected: int) -> None:
    result = title_to_number(columnTitle)
    assert (
        result == expected
    ), f"columnTitle: {columnTitle}, expected: {expected}, result: {result}"
