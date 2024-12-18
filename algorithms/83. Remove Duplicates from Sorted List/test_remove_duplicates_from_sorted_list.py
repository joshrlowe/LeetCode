import pytest  # type: ignore
from remove_duplicates_from_sorted_list import deleteDuplicates as delete_duplicates
from utils import ListNode, list_to_linked_list, linked_list_to_list
from typing import Optional


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 1, 1, 1], [1]),
        ([1], [1]),
        ([], []),
        ([1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_delete_duplicates(
    head: Optional[ListNode], expected: Optional[ListNode]
) -> None:
    linked_list = list_to_linked_list(head)
    result = linked_list_to_list(delete_duplicates(linked_list))
    assert result == expected, f"head: {head}, expected: {expected}, result: {result}"
