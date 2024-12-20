import pytest  # type: ignore
from closest_bst_value import closestValue as closest_value
from utils import TreeNode, build_tree


@pytest.mark.parametrize(
    "values, target, expected",
    [
        ([4, 2, 5, 1, 3], 3.7, 4),
        ([4, 2, 5, 1, 3], 2.1, 2),
        ([4, 2, 5, 1, 3], 0.0, 1),
        ([4, 2, 5, 1, 3], 6.0, 5),
        ([1], 0.5, 1),
        ([2, 1, 3], 3.0, 3),
        ([2, 1, 3], 2.5, 2),
        ([10, 5, 15, 3, 7, 13, 18], 12.5, 13),
        ([10, 5, 15, 3, 7, 13, 18], 17.0, 18),
        ([8, 4, 12, 2, 6, 10, 14], 11.0, 10),
    ],
)
def test_closest_value(values, target, expected):
    root = build_tree(values)
    result = closest_value(root, target)
    assert (
        result == expected
    ), f"values: {values}, target: {target}, expected: {expected}, result: {result}"
