from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Solution 1:
1. Find the middle of the linked list to divide it into two halves.
2. Reverse the second half of the list in place.
3. Merge the first half of the list with the reversed second half.

Time Complexity: O(n)
The list is traversed twice.

Space Complexity: O(1)
Only a constant amount of auxiliary space is used.
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


def list_to_array(head):
    """Helper function to convert linked list to array for easy comparison in tests."""
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def array_to_list(array):
    """Helper function to convert array to linked list for test setup."""
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for val in array[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def run_test_case(test_case_num, input_list, expected_list):
    head = array_to_list(input_list)
    expected = array_to_list(expected_list)
    solution = Solution()
    solution.reorderList(head)
    result = list_to_array(head)
    expected_result = list_to_array(expected)
    assert (
        result == expected_result
    ), f"Test case {test_case_num} failed: expected {expected_result}, got {result}"
    print(f"Test case {test_case_num} - Passed")


def test_reorderList():
    # Test case 1: Simple case with four elements
    print("Test case 1: Simple case with four elements")
    input_list = [1, 2, 3, 4]
    expected_list = [1, 4, 2, 3]
    run_test_case(1, input_list, expected_list)

    # Test case 2: Odd number of elements
    print("Test case 2: Odd number of elements")
    input_list = [1, 2, 3, 4, 5]
    expected_list = [1, 5, 2, 4, 3]
    run_test_case(2, input_list, expected_list)

    # Test case 3: Single element
    print("Test case 3: Single element")
    input_list = [1]
    expected_list = [1]
    run_test_case(3, input_list, expected_list)

    # Test case 4: Two elements
    print("Test case 4: Two elements")
    input_list = [1, 2]
    expected_list = [1, 2]
    run_test_case(4, input_list, expected_list)

    # Test case 5: Three elements
    print("Test case 5: Three elements")
    input_list = [1, 2, 3]
    expected_list = [1, 3, 2]
    run_test_case(5, input_list, expected_list)

    # Test case 6: Larger list
    print("Test case 6: Larger list")
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_list = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    run_test_case(6, input_list, expected_list)


if __name__ == "__main__":
    test_reorderList()
