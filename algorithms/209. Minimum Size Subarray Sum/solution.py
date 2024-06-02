from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float("inf")
        subSum, l = 0, 0
        for r in range(len(nums)):
            subSum += nums[r]
            while subSum >= target:
                minSize = min(minSize, r - l + 1)
                subSum -= nums[l]
                l += 1
        return minSize if minSize != float("inf") else 0


def test_minSubArrayLen():
    solution = Solution()

    # Test Case 1: Simple case with target met
    print("Test 1: Simple case with target met")
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    expected = 2
    result = solution.minSubArrayLen(target, nums)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: No subarray meets the target
    print("Test 2: No subarray meets the target")
    target = 15
    nums = [1, 2, 3, 4, 5]
    expected = 5
    result = solution.minSubArrayLen(target, nums)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Exact target met by entire array
    print("Test 3: Exact target met by entire array")
    target = 15
    nums = [1, 2, 3, 4, 5]
    expected = 5
    result = solution.minSubArrayLen(target, nums)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Single element meets the target
    print("Test 4: Single element meets the target")
    target = 4
    nums = [1, 4, 4]
    expected = 1
    result = solution.minSubArrayLen(target, nums)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Large array with valid subarrays
    print("Test 5: Large array with valid subarrays")
    target = 11
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = 2
    result = solution.minSubArrayLen(target, nums)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")


if __name__ == "__main__":
    test_minSubArrayLen()
