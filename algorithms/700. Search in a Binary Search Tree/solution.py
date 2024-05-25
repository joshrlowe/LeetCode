from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


def test_search_bst():
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

    # Helper function to check if two trees are equal
    def trees_are_equal(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and tree1.val == tree2.val:
            return trees_are_equal(tree1.left, tree2.left) and trees_are_equal(
                tree1.right, tree2.right
            )
        return False

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    tree1 = build_tree([4, 2, 7, 1, 3])
    val1 = 2
    expected1 = build_tree([2, 1, 3])
    result1 = solution.searchBST(tree1, val1)
    assert trees_are_equal(result1, expected1), f"Test Case 1 Failed"
    print("Passed")

    # Test Case 2: Node not found
    print("Test Case 2: Node not found")
    tree2 = build_tree([4, 2, 7, 1, 3])
    val2 = 5
    expected2 = None
    result2 = solution.searchBST(tree2, val2)
    assert result2 == expected2, f"Test Case 2 Failed"
    print("Passed")

    # Test Case 3: Root node search
    print("Test Case 3: Root node search")
    tree3 = build_tree([4, 2, 7, 1, 3])
    val3 = 4
    expected3 = build_tree([4, 2, 7, 1, 3])
    result3 = solution.searchBST(tree3, val3)
    assert trees_are_equal(result3, expected3), f"Test Case 3 Failed"
    print("Passed")

    # Test Case 4: Leaf node search
    print("Test Case 4: Leaf node search")
    tree4 = build_tree([4, 2, 7, 1, 3])
    val4 = 1
    expected4 = build_tree([1])
    result4 = solution.searchBST(tree4, val4)
    assert trees_are_equal(result4, expected4), f"Test Case 4 Failed"
    print("Passed")

    # Test Case 5: Empty tree
    print("Test Case 5: Empty tree")
    tree5 = build_tree([])
    val5 = 1
    expected5 = None
    result5 = solution.searchBST(tree5, val5)
    assert result5 == expected5, f"Test Case 5 Failed"
    print("Passed")

    # Test Case 6: Single node tree
    print("Test Case 6: Single node tree")
    tree6 = build_tree([1])
    val6 = 1
    expected6 = build_tree([1])
    result6 = solution.searchBST(tree6, val6)
    assert trees_are_equal(result6, expected6), f"Test Case 6 Failed"
    print("Passed")

    # Test Case 7: Right subtree search
    print("Test Case 7: Right subtree search")
    tree7 = build_tree([4, 2, 7, 1, 3, 5, 8])
    val7 = 7
    expected7 = build_tree([7, 5, 8])
    result7 = solution.searchBST(tree7, val7)
    assert trees_are_equal(result7, expected7), f"Test Case 7 Failed"
    print("Passed")


if __name__ == "__main__":
    test_search_bst()
