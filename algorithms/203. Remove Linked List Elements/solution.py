from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        while curr and curr.val == val:
            curr = head = curr.next
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


def list_to_array(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def array_to_list(array):
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for val in array[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def test_remove_elements():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    list1 = array_to_list([1, 2, 6, 3, 4, 5, 6])
    val1 = 6
    expected1 = [1, 2, 3, 4, 5]
    result1 = list_to_array(solution.removeElements(list1, val1))
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Remove all elements
    print("Test Case 2: Remove all elements")
    list2 = array_to_list([7, 7, 7, 7])
    val2 = 7
    expected2 = []
    result2 = list_to_array(solution.removeElements(list2, val2))
    assert (
        result2 == expected2
    ), f"Test Case 2 - Remove all elements Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: No elements to remove
    print("Test Case 3: No elements to remove")
    list3 = array_to_list([1, 2, 3, 4, 5])
    val3 = 6
    expected3 = [1, 2, 3, 4, 5]
    result3 = list_to_array(solution.removeElements(list3, val3))
    assert (
        result3 == expected3
    ), f"Test Case 3 - No elements to remove Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Remove from an empty list
    print("Test Case 4: Remove from an empty list")
    list4 = array_to_list([])
    val4 = 1
    expected4 = []
    result4 = list_to_array(solution.removeElements(list4, val4))
    assert (
        result4 == expected4
    ), f"Test Case 4 - Remove from an empty list Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Remove head node
    print("Test Case 5: Remove head node")
    list5 = array_to_list([1, 2, 3, 4, 5])
    val5 = 1
    expected5 = [2, 3, 4, 5]
    result5 = list_to_array(solution.removeElements(list5, val5))
    assert (
        result5 == expected5
    ), f"Test Case 5 - Remove head node Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Remove tail node
    print("Test Case 6: Remove tail node")
    list6 = array_to_list([1, 2, 3, 4, 5])
    val6 = 5
    expected6 = [1, 2, 3, 4]
    result6 = list_to_array(solution.removeElements(list6, val6))
    assert (
        result6 == expected6
    ), f"Test Case 6 - Remove tail node Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Remove multiple non-consecutive nodes
    print("Test Case 7: Remove multiple non-consecutive nodes")
    list7 = array_to_list([1, 2, 6, 3, 4, 5, 6, 7, 6])
    val7 = 6
    expected7 = [1, 2, 3, 4, 5, 7]
    result7 = list_to_array(solution.removeElements(list7, val7))
    assert (
        result7 == expected7
    ), f"Test Case 7 - Remove multiple non-consecutive nodes Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_remove_elements()
