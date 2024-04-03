def postorderTraversal(root):
    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

    result = []
    dfs(root)
    return result
