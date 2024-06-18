from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root]) if root else deque()

        while len(queue) != 0:
            result.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


def test_rightSideView():
    solution = Solution()

    # Test case 1: Regular tree
    print("Test case 1: Regular tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    expected = [1, 3, 4]
    assert solution.rightSideView(root) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Tree with only one node
    print("Test case 2: Tree with only one node")
    root = TreeNode(1)
    expected = [1]
    assert solution.rightSideView(root) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Empty tree
    print("Test case 3: Empty tree")
    root = None
    expected = []
    assert solution.rightSideView(root) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Left heavy tree
    print("Test case 4: Left heavy tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    expected = [1, 2, 3]
    assert solution.rightSideView(root) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Right heavy tree
    print("Test case 5: Right heavy tree")
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    expected = [1, 2, 3]
    assert solution.rightSideView(root) == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_rightSideView()
