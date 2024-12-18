import pytest  # type: ignore
from utils import TreeNode, build_tree
from level_order_traversal import levelOrder as level_order
from typing import Optional, List


@pytest.mark.parametrize(
    "tree, expected",
    [
        # Symmetric Trees
        ([1], [[1]]),
        ([1, 2, 2], [[1], [2, 2]]),
        ([1, 2, 2, 3, 4, 4, 3], [[1], [2, 2], [3, 4, 4, 3]]),
        # Asymmetric Trees
        ([1, 2, 3], [[1], [2, 3]]),
        ([1, 2, None, 3], [[1], [2], [3]]),
        ([1, None, 2, None, 3], [[1], [2], [3]]),
        ([1, 2, 3, None, 4, None, 5], [[1], [2, 3], [4, 5]]),
        # Complex Cases
        ([], []),
        ([1, 2, 3, 4, None, None, 5, 6, None, 7], [[1], [2, 3], [4, 5], [6, 7]]),
        ([1, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]]),
        ([1, None, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]]),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
    ],
)
def test_level_order(tree: Optional[List[int]], expected: List[List[int]]) -> None:
    result = level_order(build_tree(tree))
    assert result == expected, f"tree: {tree}, expected: {expected}, result: {result}"
