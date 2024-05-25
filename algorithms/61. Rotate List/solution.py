from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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


def test_rotate_right():
    solution = Solution()

    # Helper function to convert list to linked list
    def list_to_linkedlist(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert linked list to list
    def linkedlist_to_list(head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    head1 = list_to_linkedlist([1, 2, 3, 4, 5])
    k1 = 2
    expected1 = [4, 5, 1, 2, 3]
    result1 = linkedlist_to_list(solution.rotateRight(head1, k1))
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single element
    print("Test Case 2: Single element")
    head2 = list_to_linkedlist([1])
    k2 = 0
    expected2 = [1]
    result2 = linkedlist_to_list(solution.rotateRight(head2, k2))
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Empty list
    print("Test Case 3: Empty list")
    head3 = list_to_linkedlist([])
    k3 = 1
    expected3 = []
    result3 = linkedlist_to_list(solution.rotateRight(head3, k3))
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Rotate more than length
    print("Test Case 4: Rotate more than length")
    head4 = list_to_linkedlist([0, 1, 2])
    k4 = 4
    expected4 = [2, 0, 1]
    result4 = linkedlist_to_list(solution.rotateRight(head4, k4))
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Rotate exactly length
    print("Test Case 5: Rotate exactly length")
    head5 = list_to_linkedlist([1, 2, 3, 4, 5])
    k5 = 5
    expected5 = [1, 2, 3, 4, 5]
    result5 = linkedlist_to_list(solution.rotateRight(head5, k5))
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Rotate zero times
    print("Test Case 6: Rotate zero times")
    head6 = list_to_linkedlist([1, 2, 3])
    k6 = 0
    expected6 = [1, 2, 3]
    result6 = linkedlist_to_list(solution.rotateRight(head6, k6))
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Large k value
    print("Test Case 7: Large k value")
    head7 = list_to_linkedlist([1, 2, 3, 4, 5])
    k7 = 10
    expected7 = [1, 2, 3, 4, 5]
    result7 = linkedlist_to_list(solution.rotateRight(head7, k7))
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_rotate_right()
