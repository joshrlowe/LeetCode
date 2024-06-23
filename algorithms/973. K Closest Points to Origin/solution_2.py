import heapq
from typing import List


"""
MinHeap Solution
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res


def test_kClosest():
    solution = Solution()

    # Test case 1: Regular case with multiple points
    print("Test case 1: Regular case with multiple points")
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 2
    expected = [[-2, 2], [0, 1]]
    result = solution.kClosest(points, k)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: Single point
    print("Test case 2: Single point")
    points = [[1, 1]]
    k = 1
    expected = [[1, 1]]
    result = solution.kClosest(points, k)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: k equals number of points
    print("Test case 3: k equals number of points")
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 4
    expected = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    result = solution.kClosest(points, k)
    assert sorted(result) == sorted(expected), "Test case 3 failed"
    print("Passed")

    # Test case 4: k is 0 (should return empty list)
    print("Test case 4: k is 0")
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 0
    expected = []
    result = solution.kClosest(points, k)
    assert result == expected, "Test case 4 failed"
    print("Passed")


if __name__ == "__main__":
    test_kClosest()
