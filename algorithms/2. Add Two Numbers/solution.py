from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
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


def test_add_two_numbers():
    solution = Solution()

    # Test case 1: Basic case with no carry
    print("Test case 1: Basic case with no carry")
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [7, 0, 8]  # 342 + 465 = 807
    print("Passed")

    # Test case 2: Different lengths with carry
    print("Test case 2: Different lengths with carry")
    l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linkedlist([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [
        8,
        9,
        9,
        9,
        0,
        0,
        0,
        1,
    ]  # 9999999 + 9999 = 10009998
    print("Passed")

    # Test case 3: One list is empty
    print("Test case 3: One list is empty")
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([1, 2, 3])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [1, 2, 3]  # 0 + 123 = 123
    print("Passed")

    # Test case 4: Both lists are empty
    print("Test case 4: Both lists are empty")
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == []  # 0 + 0 = 0
    print("Passed")

    # Test case 5: Single digit with carry
    print("Test case 5: Single digit with carry")
    l1 = list_to_linkedlist([5])
    l2 = list_to_linkedlist([5])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0, 1]  # 5 + 5 = 10
    print("Passed")

    # Test case 6: Multiple carries
    print("Test case 6: Multiple carries")
    l1 = list_to_linkedlist([9, 9, 9])
    l2 = list_to_linkedlist([1])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0, 0, 0, 1]  # 999 + 1 = 1000
    print("Passed")


if __name__ == "__main__":
    test_add_two_numbers()
