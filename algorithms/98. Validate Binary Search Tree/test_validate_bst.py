import pytest  # type: ignore
from Python.validate_bst_solution_1 import isValidBST as is_valid_bst_1
from Python.validate_bst_solution_2 import isValidBST as is_valid_bst_2
from utils import TreeNode, build_tree
from typing import Optional


@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),
        ([], True),
        ([4, 3, None, 2, None, 1], True),
        ([1, None, 2, None, 3, None, 4], True),
        ([2, 2, 2], False),
        ([10, 5, 15, 3, 7, 12, 18], True),
        ([10, 5, 15, 3, 7, 6, 18], False),
        ([10, 5, 15, 3, 7, 9, 18], False),
        ([10, 5, 15, 3, 7, 6, 8], False),
        ([10, 5, 15, 3, 7, 6, 8, 18], False),
        ([10, 5, 15, 3, 7, 6, 8, 12, 18], False),
        ([10, 5, 15, 3, 7, 6, 8, 12, 18, 13], False),
        ([10, 5, 15, 3, 7, 6, 8, 12, 18, 13, 17], False),
        ([10, 5, 15, 3, 7, 6, 8, 12, 18, 13, 17, 16], False),
        ([10, 5, 15, 3, 7, 6, 8, 12, 18, 13, 17, 16, 19], False),
        ([10, 5, 15, 3, 7, 6, 8, 12, 18, 13, 17, 16, 19, 11], False),
        ([10, 5, 15, 3, 7, 6, 8, 12, 18, 13, 17, 16, 19, 11, 14], False),
    ],
)
def test_is_valid_bst(values: Optional[TreeNode], expected: bool):
    root = build_tree(values)
    result_1 = is_valid_bst_1(root)
    result_2 = is_valid_bst_2(root)
    assert (
        result_1 == expected
    ), f"values: {values}, expected: {expected}, result: {result_1}"
    assert (
        result_2 == expected
    ), f"values: {values}, expected: {expected}, result: {result_2}"
