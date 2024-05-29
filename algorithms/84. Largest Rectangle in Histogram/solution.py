from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


def test_largestRectangleArea():
    solution = Solution()

    # Test Case 1: Normal case with varied heights
    print("Test 1: Normal case with varied heights")
    heights = [2, 1, 5, 6, 2, 3]
    expected = 10
    result = solution.largestRectangleArea(heights)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: All heights the same
    print("Test 2: All heights the same")
    heights = [4, 4, 4, 4]
    expected = 16
    result = solution.largestRectangleArea(heights)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Single bar
    print("Test 3: Single bar")
    heights = [4]
    expected = 4
    result = solution.largestRectangleArea(heights)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Increasing heights
    print("Test 4: Increasing heights")
    heights = [1, 2, 3, 4, 5]
    expected = 9
    result = solution.largestRectangleArea(heights)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Decreasing heights
    print("Test 5: Decreasing heights")
    heights = [5, 4, 3, 2, 1]
    expected = 9
    result = solution.largestRectangleArea(heights)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Mixed heights with peaks and valleys
    print("Test 6: Mixed heights with peaks and valleys")
    heights = [2, 1, 2]
    expected = 3
    result = solution.largestRectangleArea(heights)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Empty array
    print("Test 7: Empty array")
    heights = []
    expected = 0
    result = solution.largestRectangleArea(heights)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Two elements
    print("Test 8: Two elements")
    heights = [2, 1]
    expected = 2
    result = solution.largestRectangleArea(heights)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_largestRectangleArea()
