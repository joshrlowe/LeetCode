from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            nonlocal maxSum
            if not node:
                return 0
            left = max(postorder(node.left), 0)
            right = max(postorder(node.right), 0)
            maxSum = max(maxSum, node.val + left + right)
            return node.val + max(left, right)

        maxSum = root.val
        postorder(root)
        return maxSum


def test_maxPathSum():
    solution = Solution()

    # Test case 1: Regular tree with mixed values
    print("Test case 1: Regular tree with mixed values")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    expected = 6
    assert solution.maxPathSum(root) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Tree with all negative values
    print("Test case 2: Tree with all negative values")
    root = TreeNode(-10)
    root.left = TreeNode(-20)
    root.right = TreeNode(-30)
    expected = -10
    assert solution.maxPathSum(root) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Single node tree
    print("Test case 3: Single node tree")
    root = TreeNode(5)
    expected = 5
    assert solution.maxPathSum(root) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Tree with mixed positive and negative values
    print("Test case 4: Tree with mixed positive and negative values")
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = 42
    assert solution.maxPathSum(root) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Tree with single path
    print("Test case 5: Tree with single path")
    root = TreeNode(10)
    root.left = TreeNode(9)
    root.left.left = TreeNode(8)
    expected = 27
    assert solution.maxPathSum(root) == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_maxPathSum()
