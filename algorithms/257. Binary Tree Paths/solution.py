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