# Recursive Solution
# O(n) Time Complexity
# O(h) Space Complexity
def preorderTraversal(root):
    result = []

    def dfs(node):
        if node:
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_preorder_traversal():
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
    expected1 = [1, 2, 3]
    result1 = preorderTraversal(tree1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Empty tree
    print("Test Case 2: Empty tree")
    tree2 = build_tree([])
    expected2 = []
    result2 = preorderTraversal(tree2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single node
    print("Test Case 3: Single node")
    tree3 = build_tree([1])
    expected3 = [1]
    result3 = preorderTraversal(tree3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Left skewed tree
    print("Test Case 4: Left skewed tree")
    tree4 = build_tree([1, 2, None, 3, None, 4])
    expected4 = [1, 2, 3, 4]
    result4 = preorderTraversal(tree4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Right skewed tree
    print("Test Case 5: Right skewed tree")
    tree5 = build_tree([1, None, 2, None, 3, None, 4])
    expected5 = [1, 2, 3, 4]
    result5 = preorderTraversal(tree5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Full binary tree
    print("Test Case 6: Full binary tree")
    tree6 = build_tree([1, 2, 3, 4, 5, 6, 7])
    expected6 = [1, 2, 4, 5, 3, 6, 7]
    result6 = preorderTraversal(tree6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Complex tree
    print("Test Case 7: Complex tree")
    tree7 = build_tree([1, 2, 3, None, 4, None, 5, 6, None, None, 7])
    expected7 = [1, 2, 4, 6, 3, 5, 7]
    result7 = preorderTraversal(tree7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_preorder_traversal()
