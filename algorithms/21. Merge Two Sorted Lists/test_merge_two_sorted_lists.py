import pytest  # type: ignore
from merge_two_sorted_lists import mergeTwoLists as merge_two_lists
from utils import ListNode, array_to_list, list_to_array
from typing import List, Optional


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [0], [0]),
        ([], [], []),
        ([1, 5, 9], [2, 6, 10], [1, 2, 5, 6, 9, 10]),
        ([1, 2, 3], [2, 3, 4], [1, 2, 2, 3, 3, 4]),
        ([5], [10], [5, 10]),
        ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
    ],
)
def test_merge_two_lists(
    list1: List[int], list2: List[int], expected: List[int]
) -> None:
    l1 = array_to_list(list1)
    l2 = array_to_list(list2)
    result = list_to_array(merge_two_lists(l1, l2))
    assert (
        result == expected
    ), f"list1: {list1}, list2: {list2}, expected: {expected}, result: {result}"
