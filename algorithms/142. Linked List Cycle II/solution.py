from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        cycleHead = head
        while slow != cycleHead:
            slow = slow.next
            cycleHead = cycleHead.next

        return cycleHead


def run_test_case(test_case_num, head, expected):
    solution = Solution()
    result = solution.detectCycle(head)
    assert (
        result == expected
    ), f"Test case {test_case_num} failed: expected '{expected.val if expected else None}', got '{result.val if result else None}'"
    print(f"Test case {test_case_num} - Passed")


def test_detectCycle():
    solution = Solution()

    # Test case 1: No cycle
    print("Test case 1: No cycle")
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    run_test_case(1, head, None)

    # Test case 2: Single node, no cycle
    print("Test case 2: Single node, no cycle")
    head = ListNode(1)
    run_test_case(2, head, None)

    # Test case 3: Single node with cycle
    print("Test case 3: Single node with cycle")
    head = ListNode(1)
    head.next = head
    run_test_case(3, head, head)

    # Test case 4: Two nodes, no cycle
    print("Test case 4: Two nodes, no cycle")
    head = ListNode(1)
    head.next = ListNode(2)
    run_test_case(4, head, None)

    # Test case 5: Two nodes with cycle
    print("Test case 5: Two nodes with cycle")
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    run_test_case(5, head, head)

    # Test case 6: Multiple nodes, no cycle
    print("Test case 6: Multiple nodes, no cycle")
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    head.next = second
    second.next = third
    third.next = fourth
    run_test_case(6, head, None)

    # Test case 7: Multiple nodes with cycle in the middle
    print("Test case 7: Multiple nodes with cycle in the middle")
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = second  # Cycle here
    run_test_case(7, head, second)

    # Test case 8: Multiple nodes with cycle at the end
    print("Test case 8: Multiple nodes with cycle at the end")
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    head.next = second
    second.next = third
    third.next = second  # Cycle here
    run_test_case(8, head, second)

    # Test case 9: Empty list
    print("Test case 9: Empty list")
    head = None
    run_test_case(9, head, None)


if __name__ == "__main__":
    test_detectCycle()
