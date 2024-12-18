from typing import Optional
from utils import ListNode


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    curr = head
    length = 1
    while curr.next:
        curr = curr.next
        length += 1
    k %= length
    if k != 0:
        curr.next = head
        for i in range(-1, k):
            curr = curr.next
        head = curr.next
        curr.next = None
    return head
