from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


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


def test_middle_node():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    head1 = array_to_list([1, 2, 3, 4, 5])
    expected1 = [3, 4, 5]
    result1 = list_to_array(solution.middleNode(head1))
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Even number of elements
    print("Test Case 2: Even number of elements")
    head2 = array_to_list([1, 2, 3, 4, 5, 6])
    expected2 = [4, 5, 6]
    result2 = list_to_array(solution.middleNode(head2))
    assert (
        result2 == expected2
    ), f"Test Case 2 - Even number of elements Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single element list
    print("Test Case 3: Single element list")
    head3 = array_to_list([1])
    expected3 = [1]
    result3 = list_to_array(solution.middleNode(head3))
    assert (
        result3 == expected3
    ), f"Test Case 3 - Single element list Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Two element list
    print("Test Case 4: Two element list")
    head4 = array_to_list([1, 2])
    expected4 = [2]
    result4 = list_to_array(solution.middleNode(head4))
    assert (
        result4 == expected4
    ), f"Test Case 4 - Two element list Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Large list
    print("Test Case 5: Large list")
    head5 = array_to_list(list(range(1, 101)))  # List from 1 to 100
    expected5 = list(range(51, 101))  # Middle node starts from 51
    result5 = list_to_array(solution.middleNode(head5))
    assert (
        result5 == expected5
    ), f"Test Case 5 - Large list Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: List with negative numbers
    print("Test Case 6: List with negative numbers")
    head6 = array_to_list([-3, -2, -1, 0, 1, 2, 3])
    expected6 = [0, 1, 2, 3]
    result6 = list_to_array(solution.middleNode(head6))
    assert (
        result6 == expected6
    ), f"Test Case 6 - List with negative numbers Failed: Expected {expected6}, got {result6}"
    print("Passed")


if __name__ == "__main__":
    test_middle_node()
