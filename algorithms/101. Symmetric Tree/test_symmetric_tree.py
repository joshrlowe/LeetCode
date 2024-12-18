import pytest  # type: ignore
from utils import build_tree
from symmetric_tree import isSymmetric as is_symmetric
from typing import Optional, List


@pytest.mark.parametrize(
    "tree, expected",
    [
        # Symmetric Trees
        ([], True),
        ([1], True),
        ([1, 2, 2], True),
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, 3, None], True),
        ([1, 2, 2, 3, 4, 4, 3], True),
        # Asymmetric Trees
        ([1, 2, 3], False),
        ([1, 2, 2, None, 3, None, 4], False),
        ([1, 2, 2, 3, None, None, 4], False),
        ([1, 2, 2, 3, 4, 5, 3], False),
        ([1, 2, None], False),
        ([1, None, 2], False),
        ([1, 2, 2, 3, None, None, None], False),
        ([1, 2, 2, None, 3, None, 3], False),
        # Complex Cases
        ([1, 2, 2, 3, None, None, 3], True),
        ([1, 2, 2, 3, 4, 4, 5], False),
        ([1, 2, 2, None, None, None, 3], False),
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5], True),
        (
            [1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5, 9, 10, 11, 12, 12, 11, 10, 9],
            False,
        ),
    ],
)
def test_is_symmetric(tree: Optional[List[int]], expected: bool) -> None:
    result = is_symmetric(build_tree(tree))
    assert result == expected, f"tree: {tree}, expected: {expected}, result: {result}"
