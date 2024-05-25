class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        if node.next:
            node.val, node.next.val = node.next.val, node.val
            node.next = node.next.next
        else:
            node = None


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


def test_delete_node():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    list1 = array_to_list([4, 5, 1, 9])
    node1 = list1.next  # node with value 5
    solution.deleteNode(node1)
    expected1 = [4, 1, 9]
    result1 = list_to_array(list1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Deleting the last node (special case, should not happen as per problem statement)
    print(
        "Test Case 2: Deleting the last node (special case, should not happen as per problem statement)"
    )
    list2 = array_to_list([1, 2, 3])
    node2 = list2.next.next  # node with value 3
    solution.deleteNode(node2)
    expected2 = [1, 2, 3]  # Last node cannot be deleted, list remains the same
    result2 = list_to_array(list2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Deleting the last node Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single element list (special case, should not happen as per problem statement)
    print(
        "Test Case 3: Single element list (special case, should not happen as per problem statement)"
    )
    list3 = array_to_list([1])
    node3 = list3  # node with value 1
    solution.deleteNode(node3)
    expected3 = [1]  # Single node cannot be deleted, list remains the same
    result3 = list_to_array(list3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Single element list Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Deleting head in a two-element list
    print("Test Case 4: Deleting head in a two-element list")
    list4 = array_to_list([1, 2])
    node4 = list4  # node with value 1
    solution.deleteNode(node4)
    expected4 = [2]
    result4 = list_to_array(list4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Deleting head in a two-element list Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Deleting second node in a three-element list
    print("Test Case 5: Deleting second node in a three-element list")
    list5 = array_to_list([1, 2, 3])
    node5 = list5.next  # node with value 2
    solution.deleteNode(node5)
    expected5 = [1, 3]
    result5 = list_to_array(list5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Deleting second node in a three-element list Failed: Expected {expected5}, got {result5}"
    print("Passed")


if __name__ == "__main__":
    test_delete_node()
