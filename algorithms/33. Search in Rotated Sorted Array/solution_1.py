from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        l, r = 0, len(nums) - 1
        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1


def test_search():
    solution = Solution()

    # Test Case 1: Target is in the rotated array
    print("Test 1: Target is in the rotated array")
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    expected = 4
    result = solution.search(nums, target)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Target is not in the array
    print("Test 2: Target is not in the array")
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    expected = -1
    result = solution.search(nums, target)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Array not rotated, target present
    print("Test 3: Array not rotated, target present")
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 5
    expected = 4
    result = solution.search(nums, target)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Array not rotated, target absent
    print("Test 4: Array not rotated, target absent")
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 8
    expected = -1
    result = solution.search(nums, target)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Single element array, target present
    print("Test 5: Single element array, target present")
    nums = [1]
    target = 1
    expected = 0
    result = solution.search(nums, target)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Single element array, target absent
    print("Test 6: Single element array, target absent")
    nums = [1]
    target = 0
    expected = -1
    result = solution.search(nums, target)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Large array, target present
    print("Test 7: Large array, target present")
    nums = list(range(1000, 5000)) + list(range(1, 1000))
    target = 3000
    expected = nums.index(target)
    result = solution.search(nums, target)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Large array, target absent
    print("Test 8: Large array, target absent")
    nums = list(range(1000, 5000)) + list(range(1, 1000))
    target = 5000
    expected = -1
    result = solution.search(nums, target)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")

    # Test Case 9: Array rotated at pivot 1
    print("Test 9: Array rotated at pivot 1")
    nums = [6, 7, 8, 9, 1, 2, 3, 4, 5]
    target = 9
    expected = 3
    result = solution.search(nums, target)
    assert result == expected, f"Test 9 Failed: expected {expected}, got {result}"
    print("Test 9 Passed")

    # Test Case 10: Array rotated at last element
    print("Test 10: Array rotated at last element")
    nums = [2, 3, 4, 5, 6, 7, 1]
    target = 1
    expected = 6
    result = solution.search(nums, target)
    assert result == expected, f"Test 10 Failed: expected {expected}, got {result}"
    print("Test 10 Passed")


if __name__ == "__main__":
    test_search()
