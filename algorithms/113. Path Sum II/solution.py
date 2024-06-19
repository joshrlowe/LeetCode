from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(node, currentSum):
            if not node:
                return
            currentSum += node.val
            path.append(node.val)

            if not node.left and not node.right and currentSum == targetSum:
                result.append(path[:])

            backtrack(node.left, currentSum)
            backtrack(node.right, currentSum)

            currentSum -= node.val
            path.pop()

        result, path = [], []
        backtrack(root, 0)
        return result


def test_path_sum():
    solution = Solution()

    # Helper function to build a tree from a list
    def build_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        index = 1
        while queue and index < len(values):
            node = queue.pop(0)
            if values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)
            index += 1
        return root

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    tree1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    targetSum1 = 22
    expected1 = [[5, 4, 11, 2], [5, 8, 4, 5]]
    result1 = solution.pathSum(tree1, targetSum1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: No paths sum to target
    print("Test Case 2: No paths sum to target")
    tree2 = build_tree([1, 2, 3])
    targetSum2 = 5
    expected2 = []
    result2 = solution.pathSum(tree2, targetSum2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single node equals target
    print("Test Case 3: Single node equals target")
    tree3 = build_tree([1])
    targetSum3 = 1
    expected3 = [[1]]
    result3 = solution.pathSum(tree3, targetSum3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single node does not equal target
    print("Test Case 4: Single node does not equal target")
    tree4 = build_tree([1])
    targetSum4 = 2
    expected4 = []
    result4 = solution.pathSum(tree4, targetSum4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Multiple paths
    print("Test Case 5: Multiple paths")
    tree5 = build_tree([1, 2, 3, None, 4, None, 5])
    targetSum5 = 6
    expected5 = []
    result5 = solution.pathSum(tree5, targetSum5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Complex tree
    print("Test Case 6: Complex tree")
    tree6 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    targetSum6 = 26
    expected6 = [[5, 8, 13]]
    result6 = solution.pathSum(tree6, targetSum6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Tree with negative numbers
    print("Test Case 7: Tree with negative numbers")
    tree7 = build_tree([-2, None, -3])
    targetSum7 = -5
    expected7 = [[-2, -3]]
    result7 = solution.pathSum(tree7, targetSum7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Large balanced tree
    print("Test Case 8: Large balanced tree")
    tree8 = build_tree([i for i in range(1, 32)])
    targetSum8 = 49
    expected8 = [[1, 3, 6, 13, 26]]
    result8 = solution.pathSum(tree8, targetSum8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_path_sum()
