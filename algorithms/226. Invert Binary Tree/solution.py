from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right = left
        root.left = right
        return root


def test_invertTree():
    solution = Solution()

    # Helper function to convert tree to list (level order traversal) for easy comparison
    def level_order_traversal(root):
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # Test case 1: Regular tree
    print("Test case 1: Regular tree")
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    result = solution.invertTree(root)
    expected = [4, 7, 2, 9, 6, 3, 1]
    assert level_order_traversal(result) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Tree with only one node
    print("Test case 2: Tree with only one node")
    root = TreeNode(1)
    result = solution.invertTree(root)
    expected = [1]
    assert level_order_traversal(result) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Empty tree
    print("Test case 3: Empty tree")
    root = None
    result = solution.invertTree(root)
    expected = []
    assert level_order_traversal(result) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Left heavy tree
    print("Test case 4: Left heavy tree")
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    result = solution.invertTree(root)
    expected = [4, 2, 1]
    assert level_order_traversal(result) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Right heavy tree
    print("Test case 5: Right heavy tree")
    root = TreeNode(4)
    root.right = TreeNode(7)
    root.right.right = TreeNode(9)
    result = solution.invertTree(root)
    expected = [4, 7, 9]
    assert level_order_traversal(result) == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_invertTree()
