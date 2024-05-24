from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


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


def test_delete_duplicates():
    solution = Solution()

    # Test case 1: Basic case with duplicates
    print("Test case 1: Basic case with duplicates")
    head = list_to_linkedlist([1, 1, 2])
    expected = [1, 2]
    result = linkedlist_to_list(solution.deleteDuplicates(head))
    assert result == expected
    print("Passed")

    # Test case 2: Multiple duplicates in a row
    print("Test case 2: Multiple duplicates in a row")
    head = list_to_linkedlist([1, 1, 2, 3, 3])
    expected = [1, 2, 3]
    result = linkedlist_to_list(solution.deleteDuplicates(head))
    assert result == expected
    print("Passed")

    # Test case 3: No duplicates
    print("Test case 3: No duplicates")
    head = list_to_linkedlist([1, 2, 3])
    expected = [1, 2, 3]
    result = linkedlist_to_list(solution.deleteDuplicates(head))
    assert result == expected
    print("Passed")

    # Test case 4: All elements are duplicates
    print("Test case 4: All elements are duplicates")
    head = list_to_linkedlist([1, 1, 1, 1])
    expected = [1]
    result = linkedlist_to_list(solution.deleteDuplicates(head))
    assert result == expected
    print("Passed")

    # Test case 5: Single element list
    print("Test case 5: Single element list")
    head = list_to_linkedlist([1])
    expected = [1]
    result = linkedlist_to_list(solution.deleteDuplicates(head))
    assert result == expected
    print("Passed")

    # Test case 6: Empty list
    print("Test case 6: Empty list")
    head = list_to_linkedlist([])
    expected = []
    result = linkedlist_to_list(solution.deleteDuplicates(head))
    assert result == expected
    print("Passed")

    # Test case 7: Long list with random duplicates
    print("Test case 7: Long list with random duplicates")
    head = list_to_linkedlist([1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6])
    expected = [1, 2, 3, 4, 5, 6]
    result = linkedlist_to_list(solution.deleteDuplicates(head))
    assert result == expected
    print("Passed")

    # Test case 8: List with alternating duplicates
    print("Test case 8: List with alternating duplicates")
    head = list_to_linkedlist([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    expected = [1, 2, 3, 4, 5]
    result = linkedlist_to_list(solution.deleteDuplicates(head))
    assert result == expected
    print("Passed")


if __name__ == "__main__":
    test_delete_duplicates()
