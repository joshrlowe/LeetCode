# Recursive Solution
# O(n) Time Complexity
# O(h) Space Complexity
def preorderTraversal(root):
        result = []
        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return result