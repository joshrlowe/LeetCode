from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]


def test_kth_largest():
    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    kthLargest1 = KthLargest(3, [4, 5, 8, 2])
    assert (
        kthLargest1.add(3) == 4
    ), f"Test Case 1 - add(3) Failed: Expected 4, got {kthLargest1.add(3)}"
    assert (
        kthLargest1.add(5) == 5
    ), f"Test Case 1 - add(5) Failed: Expected 5, got {kthLargest1.add(5)}"
    assert (
        kthLargest1.add(10) == 5
    ), f"Test Case 1 - add(10) Failed: Expected 5, got {kthLargest1.add(10)}"
    assert (
        kthLargest1.add(9) == 8
    ), f"Test Case 1 - add(9) Failed: Expected 8, got {kthLargest1.add(9)}"
    assert (
        kthLargest1.add(4) == 8
    ), f"Test Case 1 - add(4) Failed: Expected 8, got {kthLargest1.add(4)}"
    print("Passed")

    # Test Case 2: All elements added are smaller than k elements
    print("Test Case 2: All elements added are smaller than k elements")
    kthLargest2 = KthLargest(2, [5, 6])
    assert (
        kthLargest2.add(2) == 5
    ), f"Test Case 2 - add(2) Failed: Expected 5, got {kthLargest2.add(2)}"
    assert (
        kthLargest2.add(3) == 5
    ), f"Test Case 2 - add(3) Failed: Expected 5, got {kthLargest2.add(3)}"
    print("Passed")

    # Test Case 3: Single element in the initial list
    print("Test Case 3: Single element in the initial list")
    kthLargest3 = KthLargest(1, [1])
    assert (
        kthLargest3.add(2) == 2
    ), f"Test Case 3 - add(2) Failed: Expected 2, got {kthLargest3.add(2)}"
    assert (
        kthLargest3.add(-1) == 2
    ), f"Test Case 3 - add(-1) Failed: Expected 2, got {kthLargest3.add(-1)}"
    assert (
        kthLargest3.add(3) == 3
    ), f"Test Case 3 - add(3) Failed: Expected 3, got {kthLargest3.add(3)}"
    print("Passed")

    # Test Case 4: Empty initial list
    print("Test Case 4: Empty initial list")
    kthLargest4 = KthLargest(1, [])
    assert (
        kthLargest4.add(1) == 1
    ), f"Test Case 4 - add(1) Failed: Expected 1, got {kthLargest4.add(1)}"
    assert (
        kthLargest4.add(-1) == 1
    ), f"Test Case 4 - add(-1) Failed: Expected 1, got {kthLargest4.add(-1)}"
    assert (
        kthLargest4.add(0) == 1
    ), f"Test Case 4 - add(0) Failed: Expected 1, got {kthLargest4.add(0)}"
    print("Passed")

    # Test Case 5: Add elements equal to existing elements
    print("Test Case 5: Add elements equal to existing elements")
    kthLargest5 = KthLargest(3, [4, 4, 4])
    assert (
        kthLargest5.add(4) == 4
    ), f"Test Case 5 - add(4) Failed: Expected 4, got {kthLargest5.add(4)}"
    assert (
        kthLargest5.add(4) == 4
    ), f"Test Case 5 - add(4) Failed: Expected 4, got {kthLargest5.add(4)}"
    assert (
        kthLargest5.add(4) == 4
    ), f"Test Case 5 - add(4) Failed: Expected 4, got {kthLargest5.add(4)}"
    print("Passed")

    # Test Case 6: Large k value with small initial list
    print("Test Case 6: Large k value with small initial list")
    kthLargest6 = KthLargest(10, [1, 2, 3])
    assert (
        kthLargest6.add(4) == 1
    ), f"Test Case 6 - add(4) Failed: Expected 1, got {kthLargest6.add(4)}"
    assert (
        kthLargest6.add(5) == 1
    ), f"Test Case 6 - add(5) Failed: Expected 1, got {kthLargest6.add(5)}"
    assert (
        kthLargest6.add(6) == 1
    ), f"Test Case 6 - add(6) Failed: Expected 1, got {kthLargest6.add(6)}"
    assert (
        kthLargest6.add(7) == 1
    ), f"Test Case 6 - add(7) Failed: Expected 1, got {kthLargest6.add(7)}"
    print("Passed")


if __name__ == "__main__":
    test_kth_largest()
