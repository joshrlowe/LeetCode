from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result, curSum = 0, 0
        prefixSums = {0: 1}

        for num in nums:
            curSum += num
            difference = curSum - k

            result += prefixSums.get(difference, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        return result


def test_subarray_sum():
    solution = Solution()

    # Test Case 1: Basic test case
    print("Test 1: Basic test case")
    nums = [1, 1, 1]
    k = 2
    expected = 2
    result = solution.subarraySum(nums, k)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Passed")

    # Test Case 2: No subarrays sum to k
    print("Test 2: No subarrays sum to k")
    nums = [1, 2, 3]
    k = 7
    expected = 0
    result = solution.subarraySum(nums, k)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Passed")

    # Test Case 3: All elements are the same and sum to k
    print("Test 3: All elements are the same and sum to k")
    nums = [2, 2, 2, 2]
    k = 4
    expected = 3
    result = solution.subarraySum(nums, k)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Passed")

    # Test Case 4: Single element equals k
    print("Test 4: Single element equals k")
    nums = [5]
    k = 5
    expected = 1
    result = solution.subarraySum(nums, k)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Passed")

    # Test Case 5: Multiple subarrays sum to k
    print("Test 5: Multiple subarrays sum to k")
    nums = [1, 2, 3, 4, 5]
    k = 5
    expected = 2
    result = solution.subarraySum(nums, k)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Passed")

    # Test Case 6: Negative numbers in the array
    print("Test 6: Negative numbers in the array")
    nums = [1, -1, 1, -1, 1]
    k = 0
    expected = 6
    result = solution.subarraySum(nums, k)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Passed")

    # Test Case 7: Empty array
    print("Test 7: Empty array")
    nums = []
    k = 0
    expected = 0
    result = solution.subarraySum(nums, k)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Passed")


if __name__ == "__main__":
    test_subarray_sum()
