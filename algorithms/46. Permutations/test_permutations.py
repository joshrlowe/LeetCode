import pytest  # type: ignore
from Python.permutations_solution_1 import permute as permute_1
from Python.permutations_solution_2 import permute as permute_2
from typing import List


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([1], [[1]]),
        ([], [[]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1, 1], [[1, 1], [1, 1]]),
    ],
)
def test_permute(nums: List[int], expected: List[List[int]]):
    result_1 = sorted(permute_1(nums))
    result_2 = sorted(permute_2(nums))
    expected.sort()

    assert (
        result_1 == expected
    ), f"nums: {nums}, expected: {expected}, result: {result_1}"
    assert (
        result_2 == expected
    ), f"nums: {nums}, expected: {expected}, result: {result_2}"
