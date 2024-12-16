import pytest  # type: ignore
from merge_k_sorted_lists import mergeKLists as merge_k_lists
from typing import Optional, List
from utils import ListNode, array_to_list, list_to_array


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([[], [], []], []),
        ([[], [1], []], [1]),
        ([[1], [0]], [0, 1]),
        (
            [[1, 4, 5], [1, 3, 4], [2, 6], [0, 9], [3, 8]],
            [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 8, 9],
        ),
        (
            [[1000, 2000], [1500, 2500], [1001, 1002]],
            [1000, 1001, 1002, 1500, 2000, 2500],
        ),
        ([], []),
    ],
)
def test_merge_k_lists(
    lists: List[Optional[ListNode]], expected: Optional[ListNode]
) -> None:
    linked_lists = [array_to_list(lst) for lst in lists]
    result = list_to_array(merge_k_lists(linked_lists))
    assert result == expected, f"lists: {lists}, expected: {expected}, result: {result}"
