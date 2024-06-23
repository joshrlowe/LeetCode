from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if y > x:
                heapq.heappush(stones, x - y)
        return -1 * heapq.heappop(stones) if stones else 0


def test_lastStoneWeight():
    solution = Solution()

    # Test case 1: Regular case with multiple stones
    print("Test case 1: Regular case with multiple stones")
    stones = [2, 7, 4, 1, 8, 1]
    expected = 1
    result = solution.lastStoneWeight(stones)
    assert result == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: All stones with the same weight
    print("Test case 2: All stones with the same weight")
    stones = [5, 5, 5, 5]
    expected = 0
    result = solution.lastStoneWeight(stones)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Single stone
    print("Test case 3: Single stone")
    stones = [1]
    expected = 1
    result = solution.lastStoneWeight(stones)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Two stones with different weights
    print("Test case 4: Two stones with different weights")
    stones = [3, 7]
    expected = 4
    result = solution.lastStoneWeight(stones)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: No stones
    print("Test case 5: No stones")
    stones = []
    expected = 0
    result = solution.lastStoneWeight(stones)
    assert result == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_lastStoneWeight()
