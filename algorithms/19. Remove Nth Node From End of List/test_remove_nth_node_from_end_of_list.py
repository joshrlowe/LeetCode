import pytest  # type: ignore
from remove_nth_node_from_end_of_list import removeNthFromEnd as remove_nth_from_end
from utils import list_to_array, array_to_list


@pytest.mark.parametrize(
    "head, n, expected",
    [
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
        ([1, 2, 3, 4, 5], 4, [1, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ],
)
def test_remove_nth_from_end(head, n, expected):
    result = list_to_array(remove_nth_from_end(array_to_list(head), n))
    assert (
        result == expected
    ), f"list: {head}, n: {n}, expected {expected}, result {result}"
