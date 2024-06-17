from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists

        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        tail = dummy

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


def run_test_case(test_case_num, input_lists, expected_list):
    lists = [array_to_list(lst) for lst in input_lists]
    expected = array_to_list(expected_list)
    solution = Solution()
    result = solution.mergeKLists(lists)
    result_list = list_to_array(result)
    expected_result_list = list_to_array(expected)
    assert (
        result_list == expected_result_list
    ), f"Test case {test_case_num} failed: expected {expected_result_list}, got {result_list}"
    print(f"Test case {test_case_num} - Passed")


def test_mergeKLists():
    # Test case 1: Merging three sorted lists
    print("Test case 1: Merging three sorted lists")
    input_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    expected_list = [1, 1, 2, 3, 4, 4, 5, 6]
    run_test_case(1, input_lists, expected_list)

    # Test case 2: Single empty list
    print("Test case 2: Single empty list")
    input_lists = [[]]
    expected_list = []
    run_test_case(2, input_lists, expected_list)

    # Test case 3: All lists are empty
    print("Test case 3: All lists are empty")
    input_lists = [[], [], []]
    expected_list = []
    run_test_case(3, input_lists, expected_list)

    # Test case 4: Only one non-empty list
    print("Test case 4: Only one non-empty list")
    input_lists = [[], [1], []]
    expected_list = [1]
    run_test_case(4, input_lists, expected_list)

    # Test case 5: Two lists with single element each
    print("Test case 5: Two lists with single element each")
    input_lists = [[1], [0]]
    expected_list = [0, 1]
    run_test_case(5, input_lists, expected_list)

    # Test case 6: Complex case with multiple lists and elements
    print("Test case 6: Complex case with multiple lists and elements")
    input_lists = [[1, 4, 5], [1, 3, 4], [2, 6], [0, 9], [3, 8]]
    expected_list = [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 8, 9]
    run_test_case(6, input_lists, expected_list)

    # Test case 7: Large values
    print("Test case 7: Large values")
    input_lists = [[1000, 2000], [1500, 2500], [1001, 1002]]
    expected_list = [1000, 1001, 1002, 1500, 2000, 2500]
    run_test_case(7, input_lists, expected_list)


if __name__ == "__main__":
    test_mergeKLists()
