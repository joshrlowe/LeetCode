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


def test_my_linked_list():
    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)  # linked list becomes 1->2->3
    assert (
        linked_list.get(0) == 1
    ), f"Test Case 1 - get(0) Failed: Expected 1, got {linked_list.get(0)}"
    assert (
        linked_list.get(1) == 2
    ), f"Test Case 1 - get(1) Failed: Expected 2, got {linked_list.get(1)}"
    assert (
        linked_list.get(2) == 3
    ), f"Test Case 1 - get(2) Failed: Expected 3, got {linked_list.get(2)}"
    linked_list.deleteAtIndex(1)  # now the linked list is 1->3
    assert (
        linked_list.get(1) == 3
    ), f"Test Case 1 - get(1) after deleteAtIndex(1) Failed: Expected 3, got {linked_list.get(1)}"
    print("Passed")

    # Test Case 2: Add at head and delete from head
    print("Test Case 2: Add at head and delete from head")
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtHead(2)  # linked list becomes 2->1
    assert (
        linked_list.get(0) == 2
    ), f"Test Case 2 - get(0) Failed: Expected 2, got {linked_list.get(0)}"
    linked_list.deleteAtIndex(0)  # now the linked list is 1
    assert (
        linked_list.get(0) == 1
    ), f"Test Case 2 - get(0) after deleteAtIndex(0) Failed: Expected 1, got {linked_list.get(0)}"
    print("Passed")

    # Test Case 3: Add at tail and delete from tail
    print("Test Case 3: Add at tail and delete from tail")
    linked_list = MyLinkedList()
    linked_list.addAtTail(1)
    linked_list.addAtTail(2)  # linked list becomes 1->2
    assert (
        linked_list.get(1) == 2
    ), f"Test Case 3 - get(1) Failed: Expected 2, got {linked_list.get(1)}"
    linked_list.deleteAtIndex(1)  # now the linked list is 1
    assert (
        linked_list.get(1) == -1
    ), f"Test Case 3 - get(1) after deleteAtIndex(1) Failed: Expected -1, got {linked_list.get(1)}"
    print("Passed")

    # Test Case 4: Add at index out of bounds
    print("Test Case 4: Add at index out of bounds")
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    result = linked_list.addAtIndex(2, 2)  # index is out of bounds
    assert (
        result == -1
    ), f"Test Case 4 - addAtIndex(2, 2) Failed: Expected -1, got {result}"
    print("Passed")

    # Test Case 5: Delete at index out of bounds
    print("Test Case 5: Delete at index out of bounds")
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtTail(2)
    result = linked_list.deleteAtIndex(2)  # index is out of bounds
    assert (
        result == -1
    ), f"Test Case 5 - deleteAtIndex(2) Failed: Expected -1, got {result}"
    print("Passed")

    # Test Case 6: Single element operations
    print("Test Case 6: Single element operations")
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    assert (
        linked_list.get(0) == 1
    ), f"Test Case 6 - get(0) Failed: Expected 1, got {linked_list.get(0)}"
    linked_list.deleteAtIndex(0)
    assert (
        linked_list.get(0) == -1
    ), f"Test Case 6 - get(0) after deleteAtIndex(0) Failed: Expected -1, got {linked_list.get(0)}"
    print("Passed")

    # Test Case 7: Adding multiple elements and deleting from head
    print("Test Case 7: Adding multiple elements and deleting from head")
    linked_list = MyLinkedList()
    linked_list.addAtHead(3)
    linked_list.addAtHead(2)
    linked_list.addAtHead(1)  # linked list becomes 1->2->3
    linked_list.deleteAtIndex(0)  # linked list becomes 2->3
    assert (
        linked_list.get(0) == 2
    ), f"Test Case 7 - get(0) after deleteAtIndex(0) Failed: Expected 2, got {linked_list.get(0)}"
    assert (
        linked_list.get(1) == 3
    ), f"Test Case 7 - get(1) after deleteAtIndex(0) Failed: Expected 3, got {linked_list.get(1)}"
    print("Passed")

    # Test Case 8: Complex sequence of operations
    print("Test Case 8: Complex sequence of operations")
    linked_list = MyLinkedList()
    linked_list.addAtTail(1)
    linked_list.addAtHead(2)
    linked_list.addAtIndex(1, 3)  # linked list becomes 2->3->1
    linked_list.addAtTail(4)  # linked list becomes 2->3->1->4
    linked_list.deleteAtIndex(2)  # linked list becomes 2->3->4
    assert (
        linked_list.get(0) == 2
    ), f"Test Case 8 - get(0) Failed: Expected 2, got {linked_list.get(0)}"
    assert (
        linked_list.get(1) == 3
    ), f"Test Case 8 - get(1) Failed: Expected 3, got {linked_list.get(1)}"
    assert (
        linked_list.get(2) == 4
    ), f"Test Case 8 - get(2) Failed: Expected 4, got {linked_list.get(2)}"
    print("Passed")


if __name__ == "__main__":
    test_my_linked_list()
