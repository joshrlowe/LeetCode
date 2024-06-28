class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                result.append("n")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        def dfs():
            nonlocal i
            if data[i] == "n":
                i += 1
                return None
            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        data = data.split(",")
        i = 0
        return dfs()


def test_codec():
    codec = Codec()

    # Helper function to compare two binary trees
    def compare_trees(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (
            node1.val == node2.val
            and compare_trees(node1.left, node2.left)
            and compare_trees(node1.right, node2.right)
        )

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    serialized1 = codec.serialize(root1)
    deserialized1 = codec.deserialize(serialized1)
    assert compare_trees(
        root1, deserialized1
    ), "Test Case 1 - Basic functionality test Failed"
    print("Passed")

    # Test Case 2: Single node
    print("Test Case 2: Single node")
    root2 = TreeNode(1)
    serialized2 = codec.serialize(root2)
    deserialized2 = codec.deserialize(serialized2)
    assert compare_trees(root2, deserialized2), "Test Case 2 - Single node Failed"
    print("Passed")

    # Test Case 3: Empty tree
    print("Test Case 3: Empty tree")
    root3 = None
    serialized3 = codec.serialize(root3)
    deserialized3 = codec.deserialize(serialized3)
    assert compare_trees(root3, deserialized3), "Test Case 3 - Empty tree Failed"
    print("Passed")

    # Test Case 4: Left-skewed tree
    print("Test Case 4: Left-skewed tree")
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    serialized4 = codec.serialize(root4)
    deserialized4 = codec.deserialize(serialized4)
    assert compare_trees(root4, deserialized4), "Test Case 4 - Left-skewed tree Failed"
    print("Passed")

    # Test Case 5: Right-skewed tree
    print("Test Case 5: Right-skewed tree")
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    serialized5 = codec.serialize(root5)
    deserialized5 = codec.deserialize(serialized5)
    assert compare_trees(root5, deserialized5), "Test Case 5 - Right-skewed tree Failed"
    print("Passed")

    # Test Case 6: Full binary tree
    print("Test Case 6: Full binary tree")
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.left.right = TreeNode(5)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(7)
    serialized6 = codec.serialize(root6)
    deserialized6 = codec.deserialize(serialized6)
    assert compare_trees(root6, deserialized6), "Test Case 6 - Full binary tree Failed"
    print("Passed")

    # Test Case 7: Tree with negative values
    print("Test Case 7: Tree with negative values")
    root7 = TreeNode(-1)
    root7.left = TreeNode(-2)
    root7.right = TreeNode(-3)
    serialized7 = codec.serialize(root7)
    deserialized7 = codec.deserialize(serialized7)
    assert compare_trees(
        root7, deserialized7
    ), "Test Case 7 - Tree with negative values Failed"
    print("Passed")


if __name__ == "__main__":
    test_codec()
