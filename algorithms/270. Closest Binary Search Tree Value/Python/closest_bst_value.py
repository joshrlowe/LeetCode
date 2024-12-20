from utils import TreeNode
from typing import Optional


def closestValue(root: Optional[TreeNode], target: float) -> int:
    def search(node):
        nonlocal res, minDistance
        if not node:
            return

        distance = abs(node.val - target)
        if distance <= minDistance:
            res = node.val if distance < minDistance else min(res, node.val)
            minDistance = distance

        if node.val > target:
            return search(node.left)
        if node.val < target:
            return search(node.right)

    res, minDistance = 0, float("inf")
    search(root)
    return res
