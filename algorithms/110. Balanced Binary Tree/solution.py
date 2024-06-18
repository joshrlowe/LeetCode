from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return (
            abs(self.height(root.left) - self.height(root.right)) < 2
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )


def test_isBalanced():
    solution = Solution()

    # Test case 1: Balanced tree
    print("Test case 1: Balanced tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    expected = False
    assert solution.isBalanced(root) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Unbalanced tree
    print("Test case 2: Unbalanced tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    expected = False
    assert solution.isBalanced(root) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Single node tree
    print("Test case 3: Single node tree")
    root = TreeNode(1)
    expected = True
    assert solution.isBalanced(root) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Empty tree
    print("Test case 4: Empty tree")
    root = None
    expected = True
    assert solution.isBalanced(root) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Right heavy tree
    print("Test case 5: Right heavy tree")
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    expected = False
    assert solution.isBalanced(root) == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Left heavy tree
    print("Test case 6: Left heavy tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    expected = False
    assert solution.isBalanced(root) == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_isBalanced()
