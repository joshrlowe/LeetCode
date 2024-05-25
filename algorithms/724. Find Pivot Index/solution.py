from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        partialSum = 0
        for i in range(len(nums)):
            partialSum += nums[i]
            if partialSum - nums[i] == totalSum - partialSum:
                return i
        return -1


def test_pivot_index():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [1, 7, 3, 6, 5, 6]
    expected1 = 3
    result1 = solution.pivotIndex(nums1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: No pivot index
    print("Test Case 2: No pivot index")
    nums2 = [1, 2, 3]
    expected2 = -1
    result2 = solution.pivotIndex(nums2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - No pivot index Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Pivot index at the beginning
    print("Test Case 3: Pivot index at the beginning")
    nums3 = [2, 1, -1]
    expected3 = 0
    result3 = solution.pivotIndex(nums3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Pivot index at the beginning Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Pivot index at the end
    print("Test Case 4: Pivot index at the end")
    nums4 = [-1, -1, -1, 0, 1, 1]
    expected4 = 0
    result4 = solution.pivotIndex(nums4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Pivot index at the end Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Single element array
    print("Test Case 5: Single element array")
    nums5 = [1]
    expected5 = 0
    result5 = solution.pivotIndex(nums5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Single element array Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Multiple pivot indexes
    print("Test Case 6: Multiple pivot indexes")
    nums6 = [0, 1, -1, 0]
    expected6 = 0  # The first pivot index should be returned
    result6 = solution.pivotIndex(nums6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Multiple pivot indexes Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Large array
    print("Test Case 7: Large array")
    nums7 = list(range(1, 10001))
    expected7 = -1  # No pivot index in a sequence from 1 to 10000
    result7 = solution.pivotIndex(nums7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Large array Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Array with negative numbers
    print("Test Case 8: Array with negative numbers")
    nums8 = [-1, -1, -1, 0, 1, 1, 1]
    expected8 = -1
    result8 = solution.pivotIndex(nums8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Array with negative numbers Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_pivot_index()
