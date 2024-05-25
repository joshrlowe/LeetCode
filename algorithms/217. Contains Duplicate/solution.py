from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


def test_contains_duplicate():
    solution = Solution()

    # Test Case 1: Basic functionality test with duplicates
    print("Test Case 1: Basic functionality test with duplicates")
    nums1 = [1, 2, 3, 1]
    expected1 = True
    result1 = solution.containsDuplicate(nums1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test with duplicates Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: No duplicates
    print("Test Case 2: No duplicates")
    nums2 = [1, 2, 3, 4]
    expected2 = False
    result2 = solution.containsDuplicate(nums2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - No duplicates Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: All elements the same
    print("Test Case 3: All elements the same")
    nums3 = [1, 1, 1, 1]
    expected3 = True
    result3 = solution.containsDuplicate(nums3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - All elements the same Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Empty list
    print("Test Case 4: Empty list")
    nums4 = []
    expected4 = False
    result4 = solution.containsDuplicate(nums4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Empty list Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Single element
    print("Test Case 5: Single element")
    nums5 = [1]
    expected5 = False
    result5 = solution.containsDuplicate(nums5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Single element Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Large input with duplicates
    print("Test Case 6: Large input with duplicates")
    nums6 = list(range(10000)) + [9999]
    expected6 = True
    result6 = solution.containsDuplicate(nums6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Large input with duplicates Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Large input without duplicates
    print("Test Case 7: Large input without duplicates")
    nums7 = list(range(10000))
    expected7 = False
    result7 = solution.containsDuplicate(nums7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Large input without duplicates Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Negative numbers
    print("Test Case 8: Negative numbers")
    nums8 = [-1, -2, -3, -1]
    expected8 = True
    result8 = solution.containsDuplicate(nums8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Negative numbers Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: Mix of positive and negative numbers
    print("Test Case 9: Mix of positive and negative numbers")
    nums9 = [-1, 2, -3, 2]
    expected9 = True
    result9 = solution.containsDuplicate(nums9)
    assert (
        result9 == expected9
    ), f"Test Case 9 - Mix of positive and negative numbers Failed: Expected {expected9}, got {result9}"
    print("Passed")

    # Test Case 10: Large numbers
    print("Test Case 10: Large numbers")
    nums10 = [1000000000, -1000000000, 1000000000]
    expected10 = True
    result10 = solution.containsDuplicate(nums10)
    assert (
        result10 == expected10
    ), f"Test Case 10 - Large numbers Failed: Expected {expected10}, got {result10}"
    print("Passed")


if __name__ == "__main__":
    test_contains_duplicate()
