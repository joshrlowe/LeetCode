from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res


def test_findMin():
    solution = Solution()

    # Test Case 1: Rotated at one position
    print("Test 1: Rotated at one position")
    nums = [3, 4, 5, 1, 2]
    expected = 1
    result = solution.findMin(nums)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Rotated at middle position
    print("Test 2: Rotated at middle position")
    nums = [4, 5, 6, 7, 0, 1, 2]
    expected = 0
    result = solution.findMin(nums)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Rotated at last position
    print("Test 3: Rotated at last position")
    nums = [2, 3, 4, 5, 6, 7, 1]
    expected = 1
    result = solution.findMin(nums)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Fully rotated (originally sorted array)
    print("Test 4: Fully rotated (originally sorted array)")
    nums = [1, 2, 3, 4, 5, 6, 7]
    expected = 1
    result = solution.findMin(nums)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Array with two elements
    print("Test 5: Array with two elements")
    nums = [2, 1]
    expected = 1
    result = solution.findMin(nums)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Array with negative values
    print("Test 6: Array with negative values")
    nums = [1, 2, -3, -2, -1, 0]
    expected = -3
    result = solution.findMin(nums)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Array with mix of positive and negative values
    print("Test 7: Array with mix of positive and negative values")
    nums = [4, 5, 6, -3, -2, 1, 2, 3]
    expected = -3
    result = solution.findMin(nums)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Array with minimum element at the beginning
    print("Test 8: Array with minimum element at the beginning")
    nums = [1, 5, 6, 7, 8, 9, 10]
    expected = 1
    result = solution.findMin(nums)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")

    # Test Case 9: Large array with rotation
    print("Test 9: Large array with rotation")
    nums = list(range(500, 5001)) + list(range(1, 500))
    expected = 1
    result = solution.findMin(nums)
    assert result == expected, f"Test 9 Failed: expected {expected}, got {result}"
    print("Test 9 Passed")

    # Test Case 10: Large array without rotation
    print("Test 10: Large array without rotation")
    nums = list(range(1, 5001))
    expected = 1
    result = solution.findMin(nums)
    assert result == expected, f"Test 10 Failed: expected {expected}, got {result}"
    print("Test 10 Passed")


if __name__ == "__main__":
    test_findMin()
