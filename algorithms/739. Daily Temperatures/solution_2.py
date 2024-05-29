"""
Leetcode 739. Daily Temperatures

This solution uses a monotonic stack, and traverses the list from beginning to end.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])

        return res


def test_dailyTemperatures():
    solution = Solution()

    # Test Case 1: Normal case with varied temperatures
    print("Test 1: Normal case with varied temperatures")
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: All temperatures the same
    print("Test 2: All temperatures the same")
    temperatures = [30, 30, 30, 30, 30]
    expected = [0, 0, 0, 0, 0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Strictly increasing temperatures
    print("Test 3: Strictly increasing temperatures")
    temperatures = [50, 60, 70, 80, 90]
    expected = [1, 1, 1, 1, 0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Strictly decreasing temperatures
    print("Test 4: Strictly decreasing temperatures")
    temperatures = [90, 80, 70, 60, 50]
    expected = [0, 0, 0, 0, 0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Random temperatures with no warmer days
    print("Test 5: Random temperatures with no warmer days")
    temperatures = [65, 64, 63, 62, 61, 60]
    expected = [0, 0, 0, 0, 0, 0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Mixed temperatures
    print("Test 6: Mixed temperatures")
    temperatures = [30, 40, 50, 60, 20, 10, 30, 40, 50]
    expected = [1, 1, 1, 0, 2, 1, 1, 1, 0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Single temperature
    print("Test 7: Single temperature")
    temperatures = [70]
    expected = [0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Two temperatures with increase
    print("Test 8: Two temperatures with increase")
    temperatures = [70, 80]
    expected = [1, 0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")

    # Test Case 9: Two temperatures with decrease
    print("Test 9: Two temperatures with decrease")
    temperatures = [80, 70]
    expected = [0, 0]
    result = solution.dailyTemperatures(temperatures)
    assert result == expected, f"Test 9 Failed: expected {expected}, got {result}"
    print("Test 9 Passed")


if __name__ == "__main__":
    test_dailyTemperatures()
