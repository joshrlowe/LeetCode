from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self = []
        sum = 0
        for i in nums:
            sum += i
            self.append(sum)
        return self


def test_running_sum():
    solution = Solution()

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    nums1 = [1, 2, 3, 4]
    expected1 = [1, 3, 6, 10]
    result1 = solution.runningSum(nums1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single element
    print("Test Case 2: Single element")
    nums2 = [5]
    expected2 = [5]
    result2 = solution.runningSum(nums2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: All elements are zero
    print("Test Case 3: All elements are zero")
    nums3 = [0, 0, 0, 0]
    expected3 = [0, 0, 0, 0]
    result3 = solution.runningSum(nums3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Mixed positive and negative numbers
    print("Test Case 4: Mixed positive and negative numbers")
    nums4 = [1, -2, 3, -4, 5]
    expected4 = [1, -1, 2, -2, 3]
    result4 = solution.runningSum(nums4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Increasing sequence
    print("Test Case 5: Increasing sequence")
    nums5 = [1, 2, 3, 4, 5]
    expected5 = [1, 3, 6, 10, 15]
    result5 = solution.runningSum(nums5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Decreasing sequence
    print("Test Case 6: Decreasing sequence")
    nums6 = [5, 4, 3, 2, 1]
    expected6 = [5, 9, 12, 14, 15]
    result6 = solution.runningSum(nums6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Large numbers
    print("Test Case 7: Large numbers")
    nums7 = [1000000, 2000000, 3000000]
    expected7 = [1000000, 3000000, 6000000]
    result7 = solution.runningSum(nums7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Alternating positive and negative numbers
    print("Test Case 8: Alternating positive and negative numbers")
    nums8 = [10, -10, 10, -10, 10]
    expected8 = [10, 0, 10, 0, 10]
    result8 = solution.runningSum(nums8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_running_sum()
