import pytest  # type: ignore
from inorder_traversal import inorderTraversal as inorder_traversal
from utils import TreeNode, build_tree
from typing import List, Optional


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, None, 2, 3], [1, 3, 2]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [4, 2, 5, 1, 6, 3, 7]),
        ([1, 2, None, 3, None, 4], [4, 3, 2, 1]),
        ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),
        ([3, 9, None, 15, None, 7], [7, 15, 9, 3]),
        ([3, None, 9, None, 15, None, 7], [3, 9, 15, 7]),
        ([1, 2, 3, None, 4, 5, 6, None, None, 7, 8], [2, 4, 1, 7, 5, 8, 3, 6]),
    ],
)
def test_inorder_traversal(
    values: Optional[TreeNode], expected: List[int]
) -> List[int]:
    root = build_tree(values)
    result = inorder_traversal(root)
    assert (
        result == expected
    ), f"values: {values}, expected: {expected}, result: {result}"
