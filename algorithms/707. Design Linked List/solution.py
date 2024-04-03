class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.head
        pos = 0
        while curr and pos < index:
            curr = curr.next
            pos += 1
        if not curr:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return -1
        if index == 0:
            self.addAtHead(val)
            return
        new_node = ListNode(val)
        curr = self.head
        pos = 0
        while curr and pos < index - 1:
            curr = curr.next
            pos += 1
        if not curr:
            return -1
        if curr is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        next = curr.next
        curr.next = new_node
        new_node.next = next
        next.prev = new_node
        new_node.prev = curr

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return -1
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        curr = self.head
        pos = 0
        while curr.next and pos < index - 1:
            curr = curr.next
            pos += 1
        if not curr.next:
            return -1
        if curr.next is self.tail:
            self.tail = curr
            curr.next = None
            return
        next = curr.next.next
        curr.next = next
        next.prev = curr


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
