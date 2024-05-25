from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1


def test_search():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target1 = 5
    expected1 = 4
    result1 = solution.search(nums1, target1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Target not in list
    print("Test Case 2: Target not in list")
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target2 = 11
    expected2 = -1
    result2 = solution.search(nums2, target2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Target not in list Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single element list, target present
    print("Test Case 3: Single element list, target present")
    nums3 = [1]
    target3 = 1
    expected3 = 0
    result3 = solution.search(nums3, target3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Single element list, target present Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single element list, target not present
    print("Test Case 4: Single element list, target not present")
    nums4 = [1]
    target4 = 2
    expected4 = -1
    result4 = solution.search(nums4, target4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Single element list, target not present Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Target is the first element
    print("Test Case 5: Target is the first element")
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target5 = 1
    expected5 = 0
    result5 = solution.search(nums5, target5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Target is the first element Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Target is the last element
    print("Test Case 6: Target is the last element")
    nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target6 = 10
    expected6 = 9
    result6 = solution.search(nums6, target6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Target is the last element Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Large list with target in the middle
    print("Test Case 7: Large list with target in the middle")
    nums7 = list(range(1, 10001))
    target7 = 5000
    expected7 = 4999
    result7 = solution.search(nums7, target7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Large list with target in the middle Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: List with negative numbers
    print("Test Case 8: List with negative numbers")
    nums8 = [-10, -5, -3, 0, 3, 5, 7, 9, 12]
    target8 = -3
    expected8 = 2
    result8 = solution.search(nums8, target8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - List with negative numbers Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_search()
