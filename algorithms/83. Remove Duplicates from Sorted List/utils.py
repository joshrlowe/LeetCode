class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    """Helper function to convert a list to a linked list."""
    dummy_head = ListNode(0)
    current = dummy_head
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next


def linked_list_to_list(node):
    """Helper function to convert a linked list to a list."""
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst
