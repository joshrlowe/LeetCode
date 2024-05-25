from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                subresult.append(node.val)
                result.append("->".join([str(num) for num in subresult]))
                subresult.pop()
                return
            subresult.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            subresult.pop()

        result, subresult = [], []
        dfs(root)
        return result


def test_binary_tree_paths():
    solution = Solution()

    # Helper function to build a binary tree from a list
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

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    tree1 = build_tree([1, 2, 3, None, 5])
    expected1 = ["1->2->5", "1->3"]
    result1 = solution.binaryTreePaths(tree1)
    assert sorted(result1) == sorted(
        expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single node tree
    print("Test Case 2: Single node tree")
    tree2 = build_tree([1])
    expected2 = ["1"]
    result2 = solution.binaryTreePaths(tree2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Single node tree Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Left skewed tree
    print("Test Case 3: Left skewed tree")
    tree3 = build_tree([1, 2, None, 3, None, 4])
    expected3 = ["1->2->3->4"]
    result3 = solution.binaryTreePaths(tree3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Left skewed tree Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Right skewed tree
    print("Test Case 4: Right skewed tree")
    tree4 = build_tree([1, None, 2, None, 3, None, 4])
    expected4 = ["1->2->3->4"]
    result4 = solution.binaryTreePaths(tree4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Right skewed tree Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Perfect binary tree
    print("Test Case 5: Perfect binary tree")
    tree5 = build_tree([1, 2, 3, 4, 5, 6, 7])
    expected5 = ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]
    result5 = solution.binaryTreePaths(tree5)
    assert sorted(result5) == sorted(
        expected5
    ), f"Test Case 5 - Perfect binary tree Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Full binary tree
    print("Test Case 6: Full binary tree")
    tree6 = build_tree([1, 2, 3, 4, 5, None, None, 6, 7])
    expected6 = ["1->2->4->6", "1->2->4->7", "1->2->5", "1->3"]
    result6 = solution.binaryTreePaths(tree6)
    assert sorted(result6) == sorted(
        expected6
    ), f"Test Case 6 - Full binary tree Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Tree with a single branch
    print("Test Case 7: Tree with a single branch")
    tree7 = build_tree([1, 2, None, 3, None, 4, None, 5])
    expected7 = ["1->2->3->4->5"]
    result7 = solution.binaryTreePaths(tree7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Tree with a single branch Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Empty tree
    print("Test Case 8: Empty tree")
    tree8 = build_tree([])
    expected8 = []
    result8 = solution.binaryTreePaths(tree8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Empty tree Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_binary_tree_paths()
