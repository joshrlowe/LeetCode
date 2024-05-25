from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)

        result = []
        dfs(root)
        return result


def test_inorder_traversal():
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
    tree1 = build_tree([1, None, 2, 3])
    expected1 = [1, 3, 2]
    result1 = solution.inorderTraversal(tree1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single node
    print("Test Case 2: Single node")
    tree2 = build_tree([1])
    expected2 = [1]
    result2 = solution.inorderTraversal(tree2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Empty tree
    print("Test Case 3: Empty tree")
    tree3 = build_tree([])
    expected3 = []
    result3 = solution.inorderTraversal(tree3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Full binary tree
    print("Test Case 4: Full binary tree")
    tree4 = build_tree([1, 2, 3, 4, 5, 6, 7])
    expected4 = [4, 2, 5, 1, 6, 3, 7]
    result4 = solution.inorderTraversal(tree4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Left skewed tree
    print("Test Case 5: Left skewed tree")
    tree5 = build_tree([1, 2, None, 3, None, 4])
    expected5 = [4, 3, 2, 1]
    result5 = solution.inorderTraversal(tree5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Right skewed tree
    print("Test Case 6: Right skewed tree")
    tree6 = build_tree([1, None, 2, None, 3, None, 4])
    expected6 = [1, 2, 3, 4]
    result6 = solution.inorderTraversal(tree6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Tree with only left children
    print("Test Case 7: Tree with only left children")
    tree7 = build_tree([3, 9, None, 15, None, 7])
    expected7 = [7, 15, 9, 3]
    result7 = solution.inorderTraversal(tree7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Tree with only right children
    print("Test Case 8: Tree with only right children")
    tree8 = build_tree([3, None, 9, None, 15, None, 7])
    expected8 = [3, 9, 15, 7]
    result8 = solution.inorderTraversal(tree8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: Complex tree
    print("Test Case 9: Complex tree")
    tree9 = build_tree([1, 2, 3, None, 4, 5, 6, None, None, 7, 8])
    expected9 = [2, 4, 1, 7, 5, 8, 3, 6]
    result9 = solution.inorderTraversal(tree9)
    assert (
        result9 == expected9
    ), f"Test Case 9 Failed: Expected {expected9}, got {result9}"
    print("Passed")


if __name__ == "__main__":
    test_inorder_traversal()
