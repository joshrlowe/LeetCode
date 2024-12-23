import pytest  # type: ignore
from two_sum import twoSum as two_sum


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1_000_000, 2_000_000, 3_000_000, 1_000_000], 2_000_000, [0, 3]),
        ([1, 3], 4, [0, 1]),
        ([1, 2, 3], 7, None),
    ],
)
def test_two_sum(nums, target, expected):
    result = two_sum(nums, target)
    assert (
        result == expected
    ), f"nums: {nums}, target: {target}, expected: {expected}, result: {result}"
