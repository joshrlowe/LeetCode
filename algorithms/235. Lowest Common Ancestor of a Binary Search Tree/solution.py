class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cur = root
        while True:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur


def test_lowestCommonAncestor():
    solution = Solution()

    # Test case 1: Both nodes are on different sides of the root
    print("Test case 1: Both nodes are on different sides of the root")
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = root.left  # Node with value 2
    q = root.right  # Node with value 8
    expected = root
    assert solution.lowestCommonAncestor(root, p, q) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Both nodes are on the same side of the root
    print("Test case 2: Both nodes are on the same side of the root")
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 4
    expected = root.left
    assert solution.lowestCommonAncestor(root, p, q) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: One node is the root
    print("Test case 3: One node is the root")
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = root  # Node with value 6
    q = root.left.right  # Node with value 4
    expected = root
    assert solution.lowestCommonAncestor(root, p, q) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Nodes are direct children of the root
    print("Test case 4: Nodes are direct children of the root")
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    p = root.left  # Node with value 2
    q = root.right  # Node with value 8
    expected = root
    assert solution.lowestCommonAncestor(root, p, q) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Both nodes are the same
    print("Test case 5: Both nodes are the same")
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = root.left  # Node with value 2
    q = root.left  # Node with value 2
    expected = root.left
    assert solution.lowestCommonAncestor(root, p, q) == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_lowestCommonAncestor()
