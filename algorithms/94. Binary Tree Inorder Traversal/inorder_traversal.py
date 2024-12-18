from typing import List, Optional
from utils import TreeNode


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

    result = []
    dfs(root)
    return result
