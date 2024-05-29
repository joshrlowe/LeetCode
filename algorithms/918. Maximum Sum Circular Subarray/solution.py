from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        curMin, curMax = 0, 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)

        return max(maxSum, sum(nums) - minSum) if maxSum > 0 else maxSum


def test_maxSubarraySumCircular():
    solution = Solution()

    # Test Case 1: Normal case with mixed positive and negative numbers
    print("Test 1: Normal case with mixed positive and negative numbers")
    nums = [5, -3, 5]
    expected = 10
    result = solution.maxSubarraySumCircular(nums)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Mixed positive and negative numbers with minimum sum in between
    print("Test 2: Mixed positive and negative numbers with minimum sum in between")
    nums = [1, -2, 3, -2]
    expected = 3
    result = solution.maxSubarraySumCircular(nums)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Mixed positive and negative numbers with wraparound
    print("Test 3: Mixed positive and negative numbers with wraparound")
    nums = [3, -1, 2, -1]
    expected = 4
    result = solution.maxSubarraySumCircular(nums)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: All negative numbers
    print("Test 4: All negative numbers")
    nums = [-3, -2, -3]
    expected = -2
    result = solution.maxSubarraySumCircular(nums)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Single element
    print("Test 5: Single element")
    nums = [10]
    expected = 10
    result = solution.maxSubarraySumCircular(nums)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Circular subarray sum is the maximum
    print("Test 6: Circular subarray sum is the maximum")
    nums = [2, -1, 2, -1, 2, -1, 2]
    expected = 6
    result = solution.maxSubarraySumCircular(nums)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Array with all positive numbers
    print("Test 7: Array with all positive numbers")
    nums = [3, 1, 3, 2, 6]
    expected = 15
    result = solution.maxSubarraySumCircular(nums)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")


if __name__ == "__main__":
    test_maxSubarraySumCircular()
