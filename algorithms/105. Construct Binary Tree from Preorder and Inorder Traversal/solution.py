from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        mid = inorder.index(preorder[0])
        return TreeNode(
            preorder[0],
            self.buildTree(preorder[1 : mid + 1], inorder[:mid]),
            self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :]),
        )


def test_buildTree():
    solution = Solution()

    # Helper function to convert tree to list (preorder traversal) for easy comparison
    def preorder_traversal(root):
        return (
            [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)
            if root
            else []
        )

    # Test case 1: Regular tree
    print("Test case 1: Regular tree")
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = solution.buildTree(preorder, inorder)
    expected = preorder
    assert preorder_traversal(result) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Tree with only one node
    print("Test case 2: Tree with only one node")
    preorder = [1]
    inorder = [1]
    result = solution.buildTree(preorder, inorder)
    expected = preorder
    assert preorder_traversal(result) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Tree with all nodes on the left
    print("Test case 3: Tree with all nodes on the left")
    preorder = [3, 2, 1]
    inorder = [1, 2, 3]
    result = solution.buildTree(preorder, inorder)
    expected = preorder
    assert preorder_traversal(result) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Tree with all nodes on the right
    print("Test case 4: Tree with all nodes on the right")
    preorder = [1, 2, 3]
    inorder = [1, 2, 3]
    result = solution.buildTree(preorder, inorder)
    expected = preorder
    assert preorder_traversal(result) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Empty tree
    print("Test case 5: Empty tree")
    preorder = []
    inorder = []
    result = solution.buildTree(preorder, inorder)
    expected = []
    assert preorder_traversal(result) == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_buildTree()
