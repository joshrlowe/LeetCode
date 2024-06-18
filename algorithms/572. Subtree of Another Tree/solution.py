from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return (
            root.val == subRoot.val
            and self.isSameTree(root.left, subRoot.left)
            and self.isSameTree(root.right, subRoot.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


def test_isSubtree():
    solution = Solution()

    # Test case 1: Subtree is part of the tree
    print("Test case 1: Subtree is part of the tree")
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    expected = True
    assert solution.isSubtree(root, subRoot) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Subtree is not part of the tree
    print("Test case 2: Subtree is not part of the tree")
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    expected = False
    assert solution.isSubtree(root, subRoot) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Subtree is the same as the tree
    print("Test case 3: Subtree is the same as the tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    subRoot = TreeNode(1)
    subRoot.left = TreeNode(2)
    subRoot.right = TreeNode(3)
    expected = True
    assert solution.isSubtree(root, subRoot) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Empty subtree
    print("Test case 4: Empty subtree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    subRoot = None
    expected = True
    assert solution.isSubtree(root, subRoot) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Empty tree
    print("Test case 5: Empty tree")
    root = None
    subRoot = TreeNode(1)
    expected = False
    assert solution.isSubtree(root, subRoot) == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Both tree and subtree are empty
    print("Test case 6: Both tree and subtree are empty")
    root = None
    subRoot = None
    expected = True
    assert solution.isSubtree(root, subRoot) == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_isSubtree()
