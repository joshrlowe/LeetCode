from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n), Omega(log(n))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return 1 + self.maxDepth(root.left)
        elif not root.left and root.right:
            return 1 + self.maxDepth(root.right)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))