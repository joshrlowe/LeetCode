from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

def test_isSameTree():
    solution = Solution()

    # Test case 1: Both trees are identical
    print("Test case 1: Both trees are identical")
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    expected = True
    assert solution.isSameTree(p, q) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Trees have different structures
    print("Test case 2: Trees have different structures")
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    expected = False
    assert solution.isSameTree(p, q) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Trees have different values
    print("Test case 3: Trees have different values")
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    expected = False
    assert solution.isSameTree(p, q) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: One tree is empty, the other is not
    print("Test case 4: One tree is empty, the other is not")
    p = None
    q = TreeNode(1)
    expected = False
    assert solution.isSameTree(p, q) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Both trees are empty
    print("Test case 5: Both trees are empty")
    p = None
    q = None
    expected = True
    assert solution.isSameTree(p, q) == expected, "Test case 5 failed"
    print("Passed")

if __name__ == "__main__":
    test_isSameTree()
