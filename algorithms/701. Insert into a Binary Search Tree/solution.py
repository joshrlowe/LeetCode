from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root


def tree_to_list(root):
    """Helper function to convert binary tree to list for easy comparison in tests."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    # Remove trailing Nones to match expected output more cleanly
    while result and result[-1] is None:
        result.pop()
    return result


def list_to_tree(values):
    """Helper function to convert list to binary tree for test setup."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def run_test_case(test_case_num, root_list, val, expected_list):
    root = list_to_tree(root_list)
    expected = list_to_tree(expected_list)
    solution = Solution()
    result = solution.insertIntoBST(root, val)
    result_list = tree_to_list(result)
    expected_result_list = tree_to_list(expected)
    assert (
        result_list == expected_result_list
    ), f"Test case {test_case_num} failed: expected {expected_result_list}, got {result_list}"
    print(f"Test case {test_case_num} - Passed")


def test_insertIntoBST():
    # Test case 1: Insert into an empty tree
    print("Test case 1: Insert into an empty tree")
    root_list = []
    val = 5
    expected_list = [5]
    run_test_case(1, root_list, val, expected_list)

    # Test case 2: Insert into a single-node tree
    print("Test case 2: Insert into a single-node tree")
    root_list = [4]
    val = 2
    expected_list = [4, 2]
    run_test_case(2, root_list, val, expected_list)

    # Test case 3: Insert as right child
    print("Test case 3: Insert as right child")
    root_list = [4]
    val = 5
    expected_list = [4, None, 5]
    run_test_case(3, root_list, val, expected_list)

    # Test case 4: Insert into left subtree
    print("Test case 4: Insert into left subtree")
    root_list = [4, 2, 7]
    val = 1
    expected_list = [4, 2, 7, 1]
    run_test_case(4, root_list, val, expected_list)

    # Test case 5: Insert into right subtree
    print("Test case 5: Insert into right subtree")
    root_list = [4, 2, 7]
    val = 5
    expected_list = [4, 2, 7, None, None, 5]
    run_test_case(5, root_list, val, expected_list)

    # Test case 6: Insert deeper in the tree
    print("Test case 6: Insert deeper in the tree")
    root_list = [4, 2, 7, 1, 3]
    val = 6
    expected_list = [4, 2, 7, 1, 3, 6]
    run_test_case(6, root_list, val, expected_list)


if __name__ == "__main__":
    test_insertIntoBST()
