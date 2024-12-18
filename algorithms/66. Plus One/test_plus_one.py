import pytest  # type: ignore
from plus_one import plusOne as plus_one
from typing import List


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([0], [1]),
        ([0, 0, 0], [0, 0, 1]),
        ([1, 2, 3], [1, 2, 4]),
        ([9], [1, 0]),
        ([1, 2, 9], [1, 3, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([2, 9, 9, 9], [3, 0, 0, 0]),
    ],
)
def test_plus_one(digits: List[int], expected: List[int]) -> None:
    result = plus_one(digits)
    assert (
        result == expected
    ), f"digits: {digits}, expected: {expected}, result: {result}"
