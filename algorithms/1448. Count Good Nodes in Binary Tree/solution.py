class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            result = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            result += dfs(node.left, maxVal)
            result += dfs(node.right, maxVal)
            return result

        return dfs(root, root.val)


def test_goodNodes():
    solution = Solution()

    # Test case 1: Regular tree with multiple good nodes
    print("Test case 1: Regular tree with multiple good nodes")
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    expected = 4
    assert solution.goodNodes(root) == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Single node tree
    print("Test case 2: Single node tree")
    root = TreeNode(1)
    expected = 1
    assert solution.goodNodes(root) == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: All nodes are good nodes
    print("Test case 3: All nodes are good nodes")
    root = TreeNode(3)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    expected = 7
    assert solution.goodNodes(root) == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: No good nodes (all decreasing values)
    print("Test case 4: No good nodes (all decreasing values)")
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    expected = 1
    assert solution.goodNodes(root) == expected, "Test case 4 failed"
    print("Passed")


if __name__ == "__main__":
    test_goodNodes()
