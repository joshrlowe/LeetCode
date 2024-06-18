from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minValue(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValue(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root


def inorder_traversal(root):
    return (
        inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
        if root
        else []
    )


def test_deleteNode():
    solution = Solution()

    # Create a sample tree for testing
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    # Test case 1: Delete a leaf node
    print("Test case 1: Delete a leaf node")
    result = solution.deleteNode(root, 2)
    expected = [3, 4, 5, 6, 7]
    assert inorder_traversal(result) == expected, f"Test case 1 failed"
    print("Passed")

    # Test case 2: Delete a node with one child
    print("Test case 2: Delete a node with one child")
    result = solution.deleteNode(root, 3)
    expected = [4, 5, 6, 7]
    assert inorder_traversal(result) == expected, f"Test case 2 failed"
    print("Passed")

    # Test case 3: Delete a node with two children
    print("Test case 3: Delete a node with two children")
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    result = solution.deleteNode(root, 5)
    expected = [2, 3, 4, 6, 7]
    assert inorder_traversal(result) == expected, f"Test case 3 failed"
    print("Passed")

    # Test case 4: Delete root node
    print("Test case 4: Delete root node")
    result = solution.deleteNode(root, 5)
    expected = [2, 3, 4, 6, 7]
    assert inorder_traversal(result) == expected, f"Test case 4 failed"
    print("Passed")

    # Test case 5: Delete non-existent key
    print("Test case 5: Delete non-existent key")
    result = solution.deleteNode(root, 10)
    expected = [2, 3, 4, 6, 7]
    assert inorder_traversal(result) == expected, f"Test case 5 failed"
    print("Passed")

    # Test case 6: Delete from an empty tree
    print("Test case 6: Delete from an empty tree")
    empty_root = None
    result = solution.deleteNode(empty_root, 5)
    expected = []
    assert inorder_traversal(result) == expected, f"Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_deleteNode()
