import pytest  # type: ignore
from rotate_list import rotateRight as rotate_right
from typing import Optional
from utils import ListNode, list_to_linked_list, linked_list_to_list


@pytest.mark.parametrize(
    "head, k, expected",
    [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1], 0, [1]),
        ([], 1, []),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3, 4, 5], 10, [1, 2, 3, 4, 5]),
    ],
)
def test_rotate_right(head: Optional[ListNode], k: int, expected: Optional[ListNode]):
    linked_list = list_to_linked_list(head)
    result = linked_list_to_list(rotate_right(linked_list, k))
    assert (
        result == expected
    ), f"head: {head}, k: {k}, expected: {expected}, result: {result}"
