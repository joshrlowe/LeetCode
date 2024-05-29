from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        curLength, maxLength = 1, 1
        lastSign = -1

        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                if lastSign != 0:
                    curLength += 1
                else:
                    curLength = 2
                lastSign = 0
            elif arr[i - 1] < arr[i]:
                if lastSign != 1:
                    curLength += 1
                else:
                    curLength = 2
                lastSign = 1
            else:
                curLength = 1
                lastSign = -1

            maxLength = max(maxLength, curLength)

        return maxLength


def test_maxTurbulenceSize():
    solution = Solution()

    # Test Case 1: Single element
    print("Test 1: Single element")
    arr = [5]
    expected = 1
    result = solution.maxTurbulenceSize(arr)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: All elements are the same
    print("Test 2: All elements are the same")
    arr = [7, 7, 7, 7]
    expected = 1
    result = solution.maxTurbulenceSize(arr)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Strictly increasing
    print("Test 3: Strictly increasing")
    arr = [1, 2, 3, 4, 5]
    expected = 2
    result = solution.maxTurbulenceSize(arr)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Strictly decreasing
    print("Test 4: Strictly decreasing")
    arr = [5, 4, 3, 2, 1]
    expected = 2
    result = solution.maxTurbulenceSize(arr)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Turbulent array
    print("Test 5: Turbulent array")
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    expected = 5
    result = solution.maxTurbulenceSize(arr)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Another turbulent array
    print("Test 6: Another turbulent array")
    arr = [4, 8, 12, 16]
    expected = 2
    result = solution.maxTurbulenceSize(arr)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Mixed sequence with turbulence
    print("Test 7: Mixed sequence with turbulence")
    arr = [100, 100, 100]
    expected = 1
    result = solution.maxTurbulenceSize(arr)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Long turbulent sequence
    print("Test 8: Long turbulent sequence")
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9, 3, 2, 1, 4, 7, 3, 2, 8, 9, 2, 3]
    expected = 5
    result = solution.maxTurbulenceSize(arr)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_maxTurbulenceSize()
