class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if not head:
            return None

        curr = head
        node_freq = {}
        while curr:
            if curr.val in node_freq:
                node_freq[curr.val] += 1
            else:
                node_freq[curr.val] = 1
            curr = curr.next

        curr = head
        while curr and node_freq[curr.val] > 1:
            curr = head = curr.next
        while curr and curr.next:
            if node_freq[curr.next.val] > 1:
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


def test_delete_duplicates_unsorted():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    head1 = array_to_list([1, 2, 3, 2, 4])
    expected1 = [1, 3, 4]
    result1 = list_to_array(solution.deleteDuplicatesUnsorted(head1))
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: No duplicates
    print("Test Case 2: No duplicates")
    head2 = array_to_list([1, 2, 3, 4])
    expected2 = [1, 2, 3, 4]
    result2 = list_to_array(solution.deleteDuplicatesUnsorted(head2))
    assert (
        result2 == expected2
    ), f"Test Case 2 - No duplicates Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: All elements are duplicates
    print("Test Case 3: All elements are duplicates")
    head3 = array_to_list([1, 1, 2, 2, 3, 3])
    expected3 = []
    result3 = list_to_array(solution.deleteDuplicatesUnsorted(head3))
    assert (
        result3 == expected3
    ), f"Test Case 3 - All elements are duplicates Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single element list
    print("Test Case 4: Single element list")
    head4 = array_to_list([1])
    expected4 = [1]
    result4 = list_to_array(solution.deleteDuplicatesUnsorted(head4))
    assert (
        result4 == expected4
    ), f"Test Case 4 - Single element list Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Consecutive duplicates
    print("Test Case 5: Consecutive duplicates")
    head5 = array_to_list([1, 2, 2, 3, 4, 4, 5])
    expected5 = [1, 3, 5]
    result5 = list_to_array(solution.deleteDuplicatesUnsorted(head5))
    assert (
        result5 == expected5
    ), f"Test Case 5 - Consecutive duplicates Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Mixed order duplicates
    print("Test Case 6: Mixed order duplicates")
    head6 = array_to_list([4, 3, 2, 3, 1, 2, 5])
    expected6 = [4, 1, 5]
    result6 = list_to_array(solution.deleteDuplicatesUnsorted(head6))
    assert (
        result6 == expected6
    ), f"Test Case 6 - Mixed order duplicates Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: All identical elements
    print("Test Case 7: All identical elements")
    head7 = array_to_list([1, 1, 1, 1, 1])
    expected7 = []
    result7 = list_to_array(solution.deleteDuplicatesUnsorted(head7))
    assert (
        result7 == expected7
    ), f"Test Case 7 - All identical elements Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Duplicates at the end
    print("Test Case 8: Duplicates at the end")
    head8 = array_to_list([1, 2, 3, 4, 4])
    expected8 = [1, 2, 3]
    result8 = list_to_array(solution.deleteDuplicatesUnsorted(head8))
    assert (
        result8 == expected8
    ), f"Test Case 8 - Duplicates at the end Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_delete_duplicates_unsorted()
