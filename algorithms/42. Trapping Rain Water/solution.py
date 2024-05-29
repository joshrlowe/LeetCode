from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        result = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                result += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                result += maxRight - height[r]

        return result


def test_trap():
    solution = Solution()

    # Test Case 1: Normal case with varied heights
    print("Test 1: Normal case with varied heights")
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected = 6
    result = solution.trap(height)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: No trapping (flat terrain)
    print("Test 2: No trapping (flat terrain)")
    height = [1, 1, 1, 1, 1]
    expected = 0
    result = solution.trap(height)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Decreasing heights
    print("Test 3: Decreasing heights")
    height = [5, 4, 3, 2, 1]
    expected = 0
    result = solution.trap(height)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Increasing heights
    print("Test 4: Increasing heights")
    height = [1, 2, 3, 4, 5]
    expected = 0
    result = solution.trap(height)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Mixed heights with trapping
    print("Test 5: Mixed heights with trapping")
    height = [3, 0, 2, 0, 4]
    expected = 7
    result = solution.trap(height)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Single element
    print("Test 6: Single element")
    height = [0]
    expected = 0
    result = solution.trap(height)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Two elements
    print("Test 7: Two elements")
    height = [1, 0]
    expected = 0
    result = solution.trap(height)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Large numbers
    print("Test 8: Large numbers")
    height = [1000, 100, 1000, 100, 1000]
    expected = 1800
    result = solution.trap(height)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_trap()
