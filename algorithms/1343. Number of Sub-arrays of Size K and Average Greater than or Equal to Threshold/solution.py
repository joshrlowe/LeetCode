from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        kSum = sum(arr[l : r + 1])
        res = 0

        while r < len(arr):
            if kSum / k >= threshold:
                res += 1
            r += 1
            if r < len(arr):
                kSum += arr[r] - arr[l]
            l += 1
        return res


def test_numOfSubarrays():
    solution = Solution()

    # Test Case 1: Simple case with threshold met
    print("Test 1: Simple case with threshold met")
    arr = [1, 2, 3, 4, 5]
    k = 3
    threshold = 3
    expected = 2
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Simple case with threshold not met
    print("Test 2: Simple case with threshold not met")
    arr = [1, 1, 1, 1, 1]
    k = 2
    threshold = 2
    expected = 0
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Single element subarrays
    print("Test 3: Single element subarrays")
    arr = [1, 2, 3, 4, 5]
    k = 1
    threshold = 3
    expected = 3
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Entire array as a single subarray
    print("Test 4: Entire array as a single subarray")
    arr = [10, 10, 10, 10]
    k = 4
    threshold = 10
    expected = 1
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Large array with multiple valid subarrays
    print("Test 5: Large array with multiple valid subarrays")
    arr = [10000] * 100000
    k = 100
    threshold = 10000
    expected = 99901
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Mixed values with threshold not met
    print("Test 6: Mixed values with threshold not met")
    arr = [1, 2, 1, 2, 1, 2, 1, 2]
    k = 4
    threshold = 2
    expected = 0
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Minimum values for arr, k, and threshold
    print("Test 7: Minimum values for arr, k, and threshold")
    arr = [1]
    k = 1
    threshold = 1
    expected = 1
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Array where no subarrays meet the threshold
    print("Test 8: Array where no subarrays meet the threshold")
    arr = [1, 2, 1, 2, 1, 2, 1, 2]
    k = 2
    threshold = 3
    expected = 0
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")

    # Test Case 9: Array with exactly one valid subarray
    print("Test 9: Array with exactly one valid subarray")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 5
    threshold = 4
    expected = 5
    result = solution.numOfSubarrays(arr, k, threshold)
    assert result == expected, f"Test 9 Failed: expected {expected}, got {result}"
    print("Test 9 Passed")


if __name__ == "__main__":
    test_numOfSubarrays()
