from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maxArea


def test_maxArea():
    solution = Solution()

    # Test Case 1: Normal case with varied heights
    print("Test 1: Normal case with varied heights")
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected = 49
    result = solution.maxArea(height)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: All heights are the same
    print("Test 2: All heights are the same")
    height = [4, 4, 4, 4, 4, 4]
    expected = 20
    result = solution.maxArea(height)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Increasing heights
    print("Test 3: Increasing heights")
    height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = 25
    result = solution.maxArea(height)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Decreasing heights
    print("Test 4: Decreasing heights")
    height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = 25
    result = solution.maxArea(height)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Only two elements
    print("Test 5: Only two elements")
    height = [1, 100]
    expected = 1
    result = solution.maxArea(height)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Large numbers
    print("Test 6: Large numbers")
    height = [10000, 1, 10000, 1, 10000]
    expected = 40000
    result = solution.maxArea(height)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Zigzag pattern
    print("Test 7: Zigzag pattern")
    height = [1, 3, 2, 5, 2, 4, 1]
    expected = 12
    result = solution.maxArea(height)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Single peak in the middle
    print("Test 8: Single peak in the middle")
    height = [1, 2, 3, 50, 3, 2, 1]
    expected = 8
    result = solution.maxArea(height)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_maxArea()
