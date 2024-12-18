from utils import TreeNode
from typing import Optional


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (
        p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    )
