from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        min_element = min(nums) if nums else 0
        max_element = max(nums) if nums else 0

        index = 0
        for i in range(min_element, max_element + 1):
            if i in frequency:
                while frequency[i] != 0:
                    nums[index] = i
                    frequency[i] -= 1
                    index += 1

        return nums


def test_sort_array():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [5, 2, 3, 1]
    expected1 = [1, 2, 3, 5]
    result1 = solution.sortArray(nums1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Already sorted array
    print("Test Case 2: Already sorted array")
    nums2 = [1, 2, 3, 4]
    expected2 = [1, 2, 3, 4]
    result2 = solution.sortArray(nums2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Already sorted array Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Reverse sorted array
    print("Test Case 3: Reverse sorted array")
    nums3 = [4, 3, 2, 1]
    expected3 = [1, 2, 3, 4]
    result3 = solution.sortArray(nums3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Reverse sorted array Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Array with duplicates
    print("Test Case 4: Array with duplicates")
    nums4 = [4, 2, 2, 8, 3, 3, 1]
    expected4 = [1, 2, 2, 3, 3, 4, 8]
    result4 = solution.sortArray(nums4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Array with duplicates Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Single element array
    print("Test Case 5: Single element array")
    nums5 = [1]
    expected5 = [1]
    result5 = solution.sortArray(nums5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Single element array Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Empty array
    print("Test Case 6: Empty array")
    nums6 = []
    expected6 = []
    result6 = solution.sortArray(nums6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Empty array Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Array with negative numbers
    print("Test Case 7: Array with negative numbers")
    nums7 = [-3, -1, -2, -4, -5]
    expected7 = [-5, -4, -3, -2, -1]
    result7 = solution.sortArray(nums7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Array with negative numbers Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Array with mixed positive and negative numbers
    print("Test Case 8: Array with mixed positive and negative numbers")
    nums8 = [3, -1, 2, -4, 0]
    expected8 = [-4, -1, 0, 2, 3]
    result8 = solution.sortArray(nums8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Array with mixed positive and negative numbers Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_sort_array()
