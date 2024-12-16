class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_array(head):
    """Helper function to convert linked list to array for easy comparison in tests."""
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def array_to_list(array):
    """Helper function to convert array to linked list for test setup."""
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for val in array[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
