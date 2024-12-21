import pytest  # type: ignore
from delete_middle_node_of_linked_list import deleteMiddle as delete_middle
from typing import List, Optional
from utils import list_to_array, array_to_list


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([1], []),
        ([1, 2], [1]),
        ([1, 2, 3], [1, 3]),
        ([1, 2, 3, 4], [1, 2, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 4, 5]),
    ],
)
def test_delete_middle(values: Optional[List[int]], expected: Optional[List[int]]):
    head = array_to_list(values)
    updated_head = delete_middle(head)
    result = list_to_array(updated_head)
    assert (
        result == expected
    ), f"values: {values}, expected: {expected}, result: {result}"
