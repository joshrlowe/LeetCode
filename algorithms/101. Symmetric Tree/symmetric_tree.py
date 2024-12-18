from typing import Optional
from utils import TreeNode


def isMirror(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.val == node2.val:
        return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
    return False


def isSymmetric(root: Optional[TreeNode]) -> bool:
    return isMirror(root.left, root.right) if root else True
