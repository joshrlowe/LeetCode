from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 == 1:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums


def test_sort_array_by_parity():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [3, 1, 2, 4]
    expected1 = [4, 2, 1, 3]  # or any order where even numbers come before odd numbers
    result1 = solution.sortArrayByParity(nums1)
    assert all(x % 2 == 0 for x in result1[: len(result1) // 2]) and all(
        x % 2 == 1 for x in result1[len(result1) // 2 :]
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: All even numbers
    print("Test Case 2: All even numbers")
    nums2 = [2, 4, 6, 8]
    expected2 = [2, 4, 6, 8]
    result2 = solution.sortArrayByParity(nums2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - All even numbers Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: All odd numbers
    print("Test Case 3: All odd numbers")
    nums3 = [1, 3, 5, 7]
    expected3 = [1, 3, 5, 7]
    result3 = solution.sortArrayByParity(nums3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - All odd numbers Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Mixed even and odd numbers with duplicates
    print("Test Case 4: Mixed even and odd numbers with duplicates")
    nums4 = [2, 3, 3, 2, 4, 1, 1, 4]
    expected4 = [2, 2, 4, 4, 3, 3, 1, 1]
    result4 = solution.sortArrayByParity(nums4)
    assert all(x % 2 == 0 for x in result4[: len(result4) // 2]) and all(
        x % 2 == 1 for x in result4[len(result4) // 2 :]
    ), f"Test Case 4 - Mixed even and odd numbers with duplicates Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Single element array
    print("Test Case 5: Single element array")
    nums5 = [1]
    expected5 = [1]
    result5 = solution.sortArrayByParity(nums5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Single element array Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Empty array
    print("Test Case 6: Empty array")
    nums6 = []
    expected6 = []
    result6 = solution.sortArrayByParity(nums6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Empty array Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Array with negative numbers
    print("Test Case 7: Array with negative numbers")
    nums7 = [-3, -1, -2, -4]
    expected7 = [
        -4,
        -2,
        -1,
        -3,
    ]  # or any order where even numbers come before odd numbers
    result7 = solution.sortArrayByParity(nums7)
    assert all(x % 2 == 0 for x in result7[: len(result7) // 2]) and all(
        x % 2 == 1 for x in result7[len(result7) // 2 :]
    ), f"Test Case 7 - Array with negative numbers Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_sort_array_by_parity()
