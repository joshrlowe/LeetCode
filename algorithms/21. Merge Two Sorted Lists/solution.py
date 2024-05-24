from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
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


def list_to_linkedlist(lst):
    """Helper function to convert a list to a linked list."""
    dummy_head = ListNode(0)
    current = dummy_head
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next


def linkedlist_to_list(node):
    """Helper function to convert a linked list to a list."""
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


def test_merge_two_lists():
    solution = Solution()

    # Test case 1: Basic case with interleaving elements
    print("Test case 1: Basic case with interleaving elements")
    list1 = list_to_linkedlist([1, 2, 4])
    list2 = list_to_linkedlist([1, 3, 4])
    expected = [1, 1, 2, 3, 4, 4]
    result = linkedlist_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected
    print("Passed")

    # Test case 2: One list is empty
    print("Test case 2: One list is empty")
    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([0])
    expected = [0]
    result = linkedlist_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected
    print("Passed")

    # Test case 3: Both lists are empty
    print("Test case 3: Both lists are empty")
    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([])
    expected = []
    result = linkedlist_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected
    print("Passed")

    # Test case 4: Lists with non-overlapping elements
    print("Test case 4: Lists with non-overlapping elements")
    list1 = list_to_linkedlist([1, 5, 9])
    list2 = list_to_linkedlist([2, 6, 10])
    expected = [1, 2, 5, 6, 9, 10]
    result = linkedlist_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected
    print("Passed")

    # Test case 5: Lists with some overlapping elements
    print("Test case 5: Lists with some overlapping elements")
    list1 = list_to_linkedlist([1, 2, 3])
    list2 = list_to_linkedlist([2, 3, 4])
    expected = [1, 2, 2, 3, 3, 4]
    result = linkedlist_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected
    print("Passed")

    # Test case 6: Lists with single element
    print("Test case 6: Lists with single element")
    list1 = list_to_linkedlist([5])
    list2 = list_to_linkedlist([10])
    expected = [5, 10]
    result = linkedlist_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected
    print("Passed")

    # Test case 7: Lists with duplicates
    print("Test case 7: Lists with duplicates")
    list1 = list_to_linkedlist([1, 1, 1])
    list2 = list_to_linkedlist([1, 1, 1])
    expected = [1, 1, 1, 1, 1, 1]
    result = linkedlist_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected
    print("Passed")


if __name__ == "__main__":
    test_merge_two_lists()
