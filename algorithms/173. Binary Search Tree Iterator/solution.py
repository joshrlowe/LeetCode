from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return self.stack != []


def test_BSTIterator():
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
    vals = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(vals)
    iterator = BSTIterator(root)
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert result == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: BST with one node
    print("Test case 2: BST with one node")
    root = TreeNode(1)
    iterator = BSTIterator(root)
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    expected = [1]
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Empty BST
    print("Test case 3: Empty BST")
    root = None
    iterator = BSTIterator(root)
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    expected = []
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: BST with left-heavy tree
    print("Test case 4: BST with left-heavy tree")
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    iterator = BSTIterator(root)
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    expected = [1, 2, 3]
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: BST with right-heavy tree
    print("Test case 5: BST with right-heavy tree")
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    iterator = BSTIterator(root)
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    expected = [1, 2, 3]
    assert result == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_BSTIterator()
