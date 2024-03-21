def inorderTraversal(root):
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
    result = []
    dfs(root)
    return result