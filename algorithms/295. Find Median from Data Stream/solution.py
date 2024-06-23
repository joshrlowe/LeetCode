import heapq


class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if self.left and self.right and -self.left[0] > self.right[0]:
            heapq.heappush(self.right, -heapq.heappop(self.left))

        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        return -1 * self.left[0]


def test_MedianFinder():
    # Test case 1: Regular sequence of numbers
    print("Test case 1: Regular sequence of numbers")
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5, "Test case 1 failed"
    mf.addNum(3)
    assert mf.findMedian() == 2, "Test case 1 failed"
    print("Passed")

    # Test case 2: Single element
    print("Test case 2: Single element")
    mf = MedianFinder()
    mf.addNum(1)
    assert mf.findMedian() == 1, "Test case 2 failed"
    print("Passed")

    # Test case 3: Two elements
    print("Test case 3: Two elements")
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5, "Test case 3 failed"
    print("Passed")

    # Test case 4: Larger sequence of numbers
    print("Test case 4: Larger sequence of numbers")
    mf = MedianFinder()
    for num in [5, 3, 8, 9, 2, 7, 6, 4, 1]:
        mf.addNum(num)
    assert mf.findMedian() == 5, "Test case 4 failed"
    print("Passed")

    # Test case 5: Sequence with negative numbers
    print("Test case 5: Sequence with negative numbers")
    mf = MedianFinder()
    for num in [-5, -3, -8, -9, -2, -7, -6, -4, -1]:
        mf.addNum(num)
    assert mf.findMedian() == -5, "Test case 5 failed"
    print("Passed")

    # Test case 6: Sequence with duplicate numbers
    print("Test case 6: Sequence with duplicate numbers")
    mf = MedianFinder()
    for num in [1, 2, 2, 3, 4, 5, 5, 5, 6]:
        mf.addNum(num)
    assert mf.findMedian() == 4, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_MedianFinder()
