from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        from collections import deque
        result = []
        d = deque()
        reverse = False

        d.append([root])
        while len(d) != 0:
            nodes = d.pop()
            next_level = []
            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                d.append(next_level)
            if reverse:
                nodes.reverse()
            reverse = not reverse
            result.append([node.val for node in nodes])
        return result