class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        if node.next:
            node.val, node.next.val = node.next.val, node.val
            node.next = node.next.next
        else:
            node = None
