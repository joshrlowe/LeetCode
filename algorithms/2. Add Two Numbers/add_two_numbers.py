from typing import Optional
from utils import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    curr = dummy_head
    carry = 0

    while l1 or l2:
        digit1 = l1.val if l1 else 0
        digit2 = l2.val if l2 else 0
        sum = digit1 + digit2 + carry

        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry > 0:
        curr.next = ListNode(carry)

    return dummy_head.next
