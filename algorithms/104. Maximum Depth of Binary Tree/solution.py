from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n), Omega(log(n))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return 1 + self.maxDepth(root.left)
        elif not root.left and root.right:
            return 1 + self.maxDepth(root.right)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def test_max_depth():
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
    tree1 = build_tree([3, 9, 20, None, None, 15, 7])
    expected1 = 3
    result1 = solution.maxDepth(tree1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single node
    print("Test Case 2: Single node")
    tree2 = build_tree([1])
    expected2 = 1
    result2 = solution.maxDepth(tree2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Empty tree
    print("Test Case 3: Empty tree")
    tree3 = build_tree([])
    expected3 = 0
    result3 = solution.maxDepth(tree3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Full binary tree
    print("Test Case 4: Full binary tree")
    tree4 = build_tree([1, 2, 3, 4, 5, 6, 7])
    expected4 = 3
    result4 = solution.maxDepth(tree4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Left skewed tree
    print("Test Case 5: Left skewed tree")
    tree5 = build_tree([1, 2, None, 3, None, 4])
    expected5 = 4
    result5 = solution.maxDepth(tree5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Right skewed tree
    print("Test Case 6: Right skewed tree")
    tree6 = build_tree([1, None, 2, None, 3, None, 4])
    expected6 = 4
    result6 = solution.maxDepth(tree6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Tree with balanced depth
    print("Test Case 7: Tree with balanced depth")
    tree7 = build_tree([1, 2, 3, 4, 5, 6, 7, 8])
    expected7 = 4
    result7 = solution.maxDepth(tree7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Tree with only left children
    print("Test Case 8: Tree with only left children")
    tree8 = build_tree([3, 9, None, 15, None, 7])
    expected8 = 4
    result8 = solution.maxDepth(tree8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: Tree with only right children
    print("Test Case 9: Tree with only right children")
    tree9 = build_tree([3, None, 9, None, 15, None, 7])
    expected9 = 4
    result9 = solution.maxDepth(tree9)
    assert (
        result9 == expected9
    ), f"Test Case 9 Failed: Expected {expected9}, got {result9}"
    print("Passed")

    # Test Case 10: Complex tree
    print("Test Case 10: Complex tree")
    tree10 = build_tree([1, 2, 3, None, 4, 5, 6, None, None, 7, 8])
    expected10 = 4
    result10 = solution.maxDepth(tree10)
    assert (
        result10 == expected10
    ), f"Test Case 10 Failed: Expected {expected10}, got {result10}"
    print("Passed")

    # Test Case 11: Large balanced tree
    print("Test Case 11: Large balanced tree")
    tree11 = build_tree([i for i in range(1, 32)])
    expected11 = 5
    result11 = solution.maxDepth(tree11)
    assert (
        result11 == expected11
    ), f"Test Case 11 Failed: Expected {expected11}, got {result11}"
    print("Passed")


if __name__ == "__main__":
    test_max_depth()
