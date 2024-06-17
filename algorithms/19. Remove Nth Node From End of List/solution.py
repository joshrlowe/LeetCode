from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


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


def run_test_case(test_case_num, input_list, n, expected_list):
    head = array_to_list(input_list)
    expected = array_to_list(expected_list)
    solution = Solution()
    result = solution.removeNthFromEnd(head, n)
    result_list = list_to_array(result)
    expected_result_list = list_to_array(expected)
    assert (
        result_list == expected_result_list
    ), f"Test case {test_case_num} failed: expected {expected_result_list}, got {result_list}"
    print(f"Test case {test_case_num} - Passed")


def test_removeNthFromEnd():
    # Test case 1: Remove the last element
    print("Test case 1: Remove the last element")
    input_list = [1, 2, 3, 4, 5]
    n = 1
    expected_list = [1, 2, 3, 4]
    run_test_case(1, input_list, n, expected_list)

    # Test case 2: Remove the first element
    print("Test case 2: Remove the first element")
    input_list = [1, 2, 3, 4, 5]
    n = 5
    expected_list = [2, 3, 4, 5]
    run_test_case(2, input_list, n, expected_list)

    # Test case 3: Remove an element from the middle
    print("Test case 3: Remove an element from the middle")
    input_list = [1, 2, 3, 4, 5]
    n = 3
    expected_list = [1, 2, 4, 5]
    run_test_case(3, input_list, n, expected_list)

    # Test case 4: Single element list
    print("Test case 4: Single element list")
    input_list = [1]
    n = 1
    expected_list = []
    run_test_case(4, input_list, n, expected_list)

    # Test case 5: Two element list, remove the last element
    print("Test case 5: Two element list, remove the last element")
    input_list = [1, 2]
    n = 1
    expected_list = [1]
    run_test_case(5, input_list, n, expected_list)

    # Test case 6: Two element list, remove the first element
    print("Test case 6: Two element list, remove the first element")
    input_list = [1, 2]
    n = 2
    expected_list = [2]
    run_test_case(6, input_list, n, expected_list)

    # Test case 7: Remove the second to last element
    print("Test case 7: Remove the second to last element")
    input_list = [1, 2, 3, 4, 5]
    n = 2
    expected_list = [1, 2, 3, 5]
    run_test_case(7, input_list, n, expected_list)


if __name__ == "__main__":
    test_removeNthFromEnd()
