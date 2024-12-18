import pytest  # type: ignore
from same_tree import isSameTree as is_same_tree
from utils import TreeNode, build_tree
from typing import Optional, List


@pytest.mark.parametrize(
    "p, q, expected",
    [
        # Identical Trees
        ([1, 2, 3], [1, 2, 3], True),
        ([1], [1], True),
        ([1, 2, None, 4], [1, 2, None, 4], True),
        ([1, None, 2], [1, None, 2], True),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
        # Structurally Different Trees
        ([1, 2], [1, None, 2], False),
        ([1, None, 2], [1, 2], False),
        ([1, 2, 3], [1, 2], False),
        ([1, 2, 3, 4], [1, 2, 3], False),
        ([1, None, 2, None, 3], [1, 2, None, None, 3], False),
        # Value Mismatches
        ([1, 2, 3], [1, 2, 4], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([1, None, 2], [1, None, 3], False),
        ([1, 2, None, 4], [1, 2, None, 5], False),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], False),
        # Empty Trees
        ([], [], True),
        ([], [1], False),
        ([1], [], False),
        # Single Node Trees
        ([1], [2], False),
        ([1], [1], True),
        ([None], [None], True),
        ([None], [1], False),
        # Complex Trees with None values
        ([1, 2, 3, None, 4], [1, 2, 3, None, 4], True),
        ([1, 2, 3, None, 4], [1, 2, 3, 4], False),
        ([1, None, 2, None, None, 3], [1, None, 2, None, 3], False),
        ([1, 2, 3, None, None, 4, 5], [1, 2, 3, None, None, 4, 6], False),
        ([1, 2, None, 4], [1, 2, None, None, 4], False),
    ],
)
def test_is_same_tree(
    p: Optional[List[int]], q: Optional[List[int]], expected: bool
) -> None:
    result = is_same_tree(build_tree(p), build_tree(q))
    assert result == expected, f"p: {p}, q: {q}, expected: {expected}, result: {result}"
