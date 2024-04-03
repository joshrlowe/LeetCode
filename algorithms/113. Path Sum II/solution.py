from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time complexity
    # O(height) space complexity - O(log(n)) if the tree is balanced
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                path_sum.append(node.val)
                if sum(path_sum) == targetSum:
                    result.append(path_sum[:])
                path_sum.pop()
                return
            path_sum.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            path_sum.pop()

        result, path_sum = [], []
        dfs(root)
        return result
