from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


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


def test_reverse_list():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    list1 = array_to_list([1, 2, 3, 4, 5])
    expected1 = [5, 4, 3, 2, 1]
    result1 = list_to_array(solution.reverseList(list1))
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single element
    print("Test Case 2: Single element")
    list2 = array_to_list([1])
    expected2 = [1]
    result2 = list_to_array(solution.reverseList(list2))
    assert (
        result2 == expected2
    ), f"Test Case 2 - Single element Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Two elements
    print("Test Case 3: Two elements")
    list3 = array_to_list([1, 2])
    expected3 = [2, 1]
    result3 = list_to_array(solution.reverseList(list3))
    assert (
        result3 == expected3
    ), f"Test Case 3 - Two elements Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Empty list
    print("Test Case 4: Empty list")
    list4 = array_to_list([])
    expected4 = []
    result4 = list_to_array(solution.reverseList(list4))
    assert (
        result4 == expected4
    ), f"Test Case 4 - Empty list Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Larger list
    print("Test Case 5: Larger list")
    list5 = array_to_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result5 = list_to_array(solution.reverseList(list5))
    assert (
        result5 == expected5
    ), f"Test Case 5 - Larger list Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: All elements the same
    print("Test Case 6: All elements the same")
    list6 = array_to_list([1, 1, 1, 1])
    expected6 = [1, 1, 1, 1]
    result6 = list_to_array(solution.reverseList(list6))
    assert (
        result6 == expected6
    ), f"Test Case 6 - All elements the same Failed: Expected {expected6}, got {result6}"
    print("Passed")


if __name__ == "__main__":
    test_reverse_list()
