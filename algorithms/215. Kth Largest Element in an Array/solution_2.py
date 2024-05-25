from typing import List
import random


class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)

            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))

            return pivot

        return quick_select(nums, k)


def test_find_kth_largest():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    expected1 = 5
    result1 = solution.findKthLargest(nums1, k1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single element
    print("Test Case 2: Single element")
    nums2 = [1]
    k2 = 1
    expected2 = 1
    result2 = solution.findKthLargest(nums2, k2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Single element Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: All elements the same
    print("Test Case 3: All elements the same")
    nums3 = [2, 2, 2, 2]
    k3 = 2
    expected3 = 2
    result3 = solution.findKthLargest(nums3, k3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - All elements the same Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: k equals length of list
    print("Test Case 4: k equals length of list")
    nums4 = [7, 10, 4, 3, 20, 15]
    k4 = 6
    expected4 = 3
    result4 = solution.findKthLargest(nums4, k4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - k equals length of list Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: k equals 1
    print("Test Case 5: k equals 1")
    nums5 = [3, 2, 1, 5, 6, 4]
    k5 = 1
    expected5 = 6
    result5 = solution.findKthLargest(nums5, k5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - k equals 1 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Negative numbers
    print("Test Case 6: Negative numbers")
    nums6 = [-1, -2, -3, -4, -5]
    k6 = 2
    expected6 = -2
    result6 = solution.findKthLargest(nums6, k6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Negative numbers Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Mixed positive and negative numbers
    print("Test Case 7: Mixed positive and negative numbers")
    nums7 = [3, -2, 1, -5, 6, 4]
    k7 = 3
    expected7 = 3
    result7 = solution.findKthLargest(nums7, k7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Mixed positive and negative numbers Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Large k value
    print("Test Case 8: Large k value")
    nums8 = [3, 2, 1, 5, 6, 4]
    k8 = 5
    expected8 = 2
    result8 = solution.findKthLargest(nums8, k8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Large k value Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_find_kth_largest()
