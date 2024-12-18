from collections import deque
from typing import List, Optional
from utils import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    d = deque()

    d.append([root])
    while len(d) != 0:
        nodes = d.popleft()
        next_level = []
        for node in nodes:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            d.append(next_level[:])
        result.append([node.val for node in nodes])

    return result
