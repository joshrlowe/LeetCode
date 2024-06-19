from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(node, currentSum):
            if not node:
                return False
            currentSum += node.val
            if not node.left and not node.right:
                return currentSum == targetSum
            return backtrack(node.left, currentSum) or backtrack(node.right, currentSum)

        return backtrack(root, 0)


def test_hasPathSum():
    solution = Solution()

    # Test case 1: Regular tree with a valid path sum
    print("Test case 1: Regular tree with a valid path sum")
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    targetSum = 22
    expected = True
    assert solution.hasPathSum(root, targetSum) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Regular tree without a valid path sum
    print("Test case 2: Regular tree without a valid path sum")
    targetSum = 26
    expected = True
    assert solution.hasPathSum(root, targetSum) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Single node tree with a valid path sum
    print("Test case 3: Single node tree with a valid path sum")
    root = TreeNode(5)
    targetSum = 5
    expected = True
    assert solution.hasPathSum(root, targetSum) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Single node tree without a valid path sum
    print("Test case 4: Single node tree without a valid path sum")
    targetSum = 1
    expected = False
    assert solution.hasPathSum(root, targetSum) == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Empty tree
    print("Test case 5: Empty tree")
    root = None
    targetSum = 0
    expected = False
    assert solution.hasPathSum(root, targetSum) == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Tree with negative values
    print("Test case 6: Tree with negative values")
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    targetSum = -5
    expected = True
    assert solution.hasPathSum(root, targetSum) == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_hasPathSum()
