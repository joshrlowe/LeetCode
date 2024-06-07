from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        maxSum = 0
        while slow:
            curSum = slow.val + stack.pop()
            maxSum = max(maxSum, curSum)
            slow = slow.next
    
        return maxSum
    

def run_test_case(test_case_num, head, expected):
    solution = Solution()
    result = solution.pairSum(head)
    assert result == expected, f"Test case {test_case_num} failed: expected {expected}, got {result}"
    print(f"Test case {test_case_num} - Passed")

def test_pairSum():
    solution = Solution()

    # Test case 1: Simple case with two elements
    print("Test case 1: Simple case with two elements")
    head = ListNode(1)
    head.next = ListNode(2)
    run_test_case(1, head, 3)

    # Test case 2: Four elements with symmetric values
    print("Test case 2: Four elements with symmetric values")
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    run_test_case(2, head, 4)

    # Test case 3: Multiple elements with increasing values
    print("Test case 3: Multiple elements with increasing values")
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(4)
    run_test_case(4, head, 5)

    # Test case 4: Multiple elements with decreasing values
    print("Test case 4: Multiple elements with decreasing values")
    head = ListNode(4)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    run_test_case(4, head, 5)

if __name__ == "__main__":
    test_pairSum()


        