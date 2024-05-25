from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isSorted(lst):
            for i in range(len(lst) - 1):
                if lst[i] >= lst[i + 1]:
                    return False
            return True

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        result = []
        inorder(root)
        return isSorted(result)


def test_is_valid_bst():
    solution = Solution()

    # Helper function to build a tree from a list
    def build_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        index = 1
        while queue and index < len(values):
            node = queue.pop(0)
            if values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)
            index += 1
        return root

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    tree1 = build_tree([2, 1, 3])
    expected1 = True
    result1 = solution.isValidBST(tree1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Not a valid BST
    print("Test Case 2: Not a valid BST")
    tree2 = build_tree([5, 1, 4, None, None, 3, 6])
    expected2 = False
    result2 = solution.isValidBST(tree2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single node
    print("Test Case 3: Single node")
    tree3 = build_tree([1])
    expected3 = True
    result3 = solution.isValidBST(tree3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Empty tree
    print("Test Case 4: Empty tree")
    tree4 = build_tree([])
    expected4 = True
    result4 = solution.isValidBST(tree4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Left skewed tree
    print("Test Case 5: Left skewed tree")
    tree5 = build_tree([4, 3, None, 2, None, 1])
    expected5 = True
    result5 = solution.isValidBST(tree5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Right skewed tree
    print("Test Case 6: Right skewed tree")
    tree6 = build_tree([1, None, 2, None, 3, None, 4])
    expected6 = True
    result6 = solution.isValidBST(tree6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Tree with duplicates
    print("Test Case 7: Tree with duplicates")
    tree7 = build_tree([2, 2, 2])
    expected7 = False
    result7 = solution.isValidBST(tree7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Large balanced BST
    print("Test Case 8: Large balanced BST")
    tree8 = build_tree([10, 5, 15, 3, 7, 12, 18])
    expected8 = True
    result8 = solution.isValidBST(tree8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: Complex invalid BST
    print("Test Case 9: Complex invalid BST")
    tree9 = build_tree([10, 5, 15, 3, 7, 6, 18])
    expected9 = False
    result9 = solution.isValidBST(tree9)
    assert (
        result9 == expected9
    ), f"Test Case 9 Failed: Expected {expected9}, got {result9}"
    print("Passed")

    # Test Case 10: Another complex invalid BST
    print("Test Case 10: Another complex invalid BST")
    tree10 = build_tree([10, 5, 15, 3, 7, 9, 18])
    expected10 = False
    result10 = solution.isValidBST(tree10)
    assert (
        result10 == expected10
    ), f"Test Case 10 Failed: Expected {expected10}, got {result10}"
    print("Passed")


if __name__ == "__main__":
    test_is_valid_bst()
