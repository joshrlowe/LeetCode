from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isSorted(lst):
            for i in range(len(lst) - 1):
                if lst[i] >= lst[i + 1]:
                    return False
            return True

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        result = []
        inorder(root)
        return isSorted(result)
