import pytest  # type: ignore
from add_two_numbers import addTwoNumbers as add_two_numbers
from utils import list_to_linked_list, linked_list_to_list


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([], [], []),
        ([5], [5], [0, 1]),
        ([9, 9, 9], [1], [0, 0, 0, 1]),
    ],
)
def test_add_two_numbers(l1, l2, expected):
    l1_linked_list = list_to_linked_list(l1)
    l2_linked_list = list_to_linked_list(l2)
    result = linked_list_to_list(add_two_numbers(l1_linked_list, l2_linked_list))
    assert (
        result == expected
    ), f"l1: {l1}, l2: {l2}, expected: {expected}, result: {result}"
