import heapq
from typing import List, Optional
from utils import ListNode


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy

    min_heap = []
    counter = 0

    for head in lists:
        if head:
            heapq.heappush(min_heap, (head.val, counter, head))
            counter += 1

    while min_heap:
        value, _, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if current.next:
            heapq.heappush(min_heap, (current.next.val, counter, current.next))
            counter += 1

    return dummy.next
