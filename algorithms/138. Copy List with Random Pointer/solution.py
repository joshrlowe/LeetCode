from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        old_to_new = {None: None}

        current = head
        while current:
            copy = Node(current.val)
            old_to_new[current] = copy
            current = current.next

        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new[current.next]
            copy.random = old_to_new[current.random]
            current = current.next

        return old_to_new[head]


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def list_to_array(head):
    """Helper function to convert linked list with random pointers to a list for easy comparison in tests."""
    if not head:
        return []

    # Create a map from node to index
    node_to_index = {}
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1

    # Create array representation
    array = []
    current = head
    while current:
        next_index = node_to_index.get(current.next, None)
        random_index = node_to_index.get(current.random, None)
        array.append((current.val, next_index, random_index))
        current = current.next

    return array


def array_to_list(array):
    """Helper function to convert an array to a linked list with random pointers for test setup."""
    if not array:
        return None

    # Create nodes
    nodes = [Node(val) for val, _, _ in array]

    # Set next and random pointers
    for i, (val, next_index, random_index) in enumerate(array):
        if next_index is not None:
            nodes[i].next = nodes[next_index]
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


def run_test_case(test_case_num, input_array, expected_array):
    head = array_to_list(input_array)
    expected = array_to_list(expected_array)
    solution = Solution()
    result = solution.copyRandomList(head)
    result_list = list_to_array(result)
    expected_result_list = list_to_array(expected)
    assert (
        result_list == expected_result_list
    ), f"Test case {test_case_num} failed: expected {expected_result_list}, got {result_list}"
    print(f"Test case {test_case_num} - Passed")


def test_copyRandomList():
    # Test case 1: Simple case with no random pointers
    print("Test case 1: Simple case with no random pointers")
    input_array = [(1, 1, None), (2, None, None)]
    expected_array = [(1, 1, None), (2, None, None)]
    run_test_case(1, input_array, expected_array)

    # Test case 2: Single element with no random pointer
    print("Test case 2: Single element with no random pointer")
    input_array = [(1, None, None)]
    expected_array = [(1, None, None)]
    run_test_case(2, input_array, expected_array)

    # Test case 3: Single element with random pointer to itself
    print("Test case 3: Single element with random pointer to itself")
    input_array = [(1, None, 0)]
    expected_array = [(1, None, 0)]
    run_test_case(3, input_array, expected_array)

    # Test case 4: Two elements with random pointers to each other
    print("Test case 4: Two elements with random pointers to each other")
    input_array = [(1, 1, 1), (2, None, 0)]
    expected_array = [(1, 1, 1), (2, None, 0)]
    run_test_case(4, input_array, expected_array)

    # Test case 5: Complex case with multiple nodes and random pointers
    print("Test case 5: Complex case with multiple nodes and random pointers")
    input_array = [(1, 1, None), (2, 2, 0), (3, None, 1)]
    expected_array = [(1, 1, None), (2, 2, 0), (3, None, 1)]
    run_test_case(5, input_array, expected_array)

    # Test case 6: Empty list
    print("Test case 6: Empty list")
    input_array = []
    expected_array = []
    run_test_case(6, input_array, expected_array)


if __name__ == "__main__":
    test_copyRandomList()
