class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if not head:
            return None

        curr = head
        node_freq = {}
        while curr:
            if curr.val in node_freq:
                node_freq[curr.val] += 1
            else:
                node_freq[curr.val] = 1
            curr = curr.next
        
        curr = head
        while curr and node_freq[curr.val] > 1:
            curr = head = curr.next
        while curr and curr.next:
            if node_freq[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head