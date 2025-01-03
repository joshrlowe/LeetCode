from typing import Optional
from utils import ListNode


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    head = ListNode()
    tail = head

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    return head.next
