from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Iterative Solution
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


def test_kthSmallest():
    solution = Solution()

    # Helper function to build a tree from a list of values
    def build_tree(vals):
        if not vals:
            return None
        mid = len(vals) // 2
        root = TreeNode(vals[mid])
        root.left = build_tree(vals[:mid])
        root.right = build_tree(vals[mid + 1 :])
        return root

    # Test case 1: Regular BST
    print("Test case 1: Regular BST")
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    k = 1
    expected = 1
    assert solution.kthSmallest(root, k) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Regular BST, k=2
    print("Test case 2: Regular BST, k=2")
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    k = 2
    expected = 2
    assert solution.kthSmallest(root, k) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: BST with one node
    print("Test case 3: BST with one node")
    root = TreeNode(1)
    k = 1
    expected = 1
    assert solution.kthSmallest(root, k) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Left-heavy BST
    print("Test case 4: Left-heavy BST")
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    k = 3
    expected = 3
    assert solution.kthSmallest(root, k) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Right-heavy BST
    print("Test case 5: Right-heavy BST")
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    k = 3
    expected = 3
    assert solution.kthSmallest(root, k) == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_kthSmallest()
