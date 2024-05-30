from typing import List


class Solution:
    def canEat(self, piles: List[int], k: int, h: int) -> bool:
        hours_to_eat = 0
        for pile in piles:
            hours_to_eat += (pile + k - 1) // k
        return hours_to_eat <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if self.canEat(piles, mid, h):
                high = mid
            else:
                low = mid + 1
        return low


def test_minEatingSpeed():
    solution = Solution()

    # Test Case 1: Simple case with small piles
    print("Test 1: Simple case with small piles")
    piles = [3, 6, 7, 11]
    h = 8
    expected = 4
    result = solution.minEatingSpeed(piles, h)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: All piles are the same
    print("Test 2: All piles are the same")
    piles = [30, 30, 30, 30]
    h = 4
    expected = 30
    result = solution.minEatingSpeed(piles, h)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Large h value allowing minimum speed
    print("Test 3: Large h value allowing minimum speed")
    piles = [1, 1, 1, 1, 1, 1, 1, 1]
    h = 100
    expected = 1
    result = solution.minEatingSpeed(piles, h)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Piles with large values and minimum h
    print("Test 4: Piles with large values and minimum h")
    piles = [1000000000, 1000000000, 1000000000]
    h = 3
    expected = 1000000000
    result = solution.minEatingSpeed(piles, h)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Mixed values with moderate h
    print("Test 5: Mixed values with moderate h")
    piles = [30, 11, 23, 4, 20]
    h = 5
    expected = 30
    result = solution.minEatingSpeed(piles, h)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Single pile
    print("Test 6: Single pile")
    piles = [1000000000]
    h = 2
    expected = 500000000
    result = solution.minEatingSpeed(piles, h)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Small piles with exact h
    print("Test 7: Small piles with exact h")
    piles = [3, 6, 7, 11]
    h = 4
    expected = 11
    result = solution.minEatingSpeed(piles, h)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Large number of small piles
    print("Test 8: Large number of small piles")
    piles = [2] * 10000
    h = 10000
    expected = 2
    result = solution.minEatingSpeed(piles, h)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_minEatingSpeed()
