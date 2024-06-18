from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal diameter
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right + 2)
            return max(left, right) + 1

        diameter = 0
        dfs(root)
        return diameter


def test_diameter_of_binary_tree():
    solution = Solution()

    # Helper function to build a binary tree from a list
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

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    tree1 = build_tree([1, 2, 3, 4, 5])
    expected1 = 3
    result1 = solution.diameterOfBinaryTree(tree1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single node tree
    print("Test Case 2: Single node tree")
    tree2 = build_tree([1])
    expected2 = 0
    result2 = solution.diameterOfBinaryTree(tree2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Single node tree Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Empty tree
    print("Test Case 3: Empty tree")
    tree3 = build_tree([])
    expected3 = 0
    result3 = solution.diameterOfBinaryTree(tree3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Empty tree Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Linear tree (left-skewed)
    print("Test Case 4: Linear tree (left-skewed)")
    tree4 = build_tree([1, 2, None, 3, None, 4, None, 5])
    expected4 = 4
    result4 = solution.diameterOfBinaryTree(tree4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Linear tree (left-skewed) Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Linear tree (right-skewed)
    print("Test Case 5: Linear tree (right-skewed)")
    tree5 = build_tree([1, None, 2, None, 3, None, 4, None, 5])
    expected5 = 4
    result5 = solution.diameterOfBinaryTree(tree5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Linear tree (right-skewed) Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Perfect binary tree
    print("Test Case 6: Perfect binary tree")
    tree6 = build_tree([1, 2, 3, 4, 5, 6, 7])
    expected6 = 4
    result6 = solution.diameterOfBinaryTree(tree6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Perfect binary tree Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Full binary tree
    print("Test Case 7: Full binary tree")
    tree7 = build_tree([1, 2, 3, 4, 5, None, None, 6, 7])
    expected7 = 4
    result7 = solution.diameterOfBinaryTree(tree7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Full binary tree Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_diameter_of_binary_tree()
