from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                if length > longest:
                    longest = length
        return longest


def test_longest_consecutive():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [100, 4, 200, 1, 3, 2]
    expected1 = 4
    result1 = solution.longestConsecutive(nums1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single element
    print("Test Case 2: Single element")
    nums2 = [1]
    expected2 = 1
    result2 = solution.longestConsecutive(nums2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: No elements
    print("Test Case 3: No elements")
    nums3 = []
    expected3 = 0
    result3 = solution.longestConsecutive(nums3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: All elements the same
    print("Test Case 4: All elements the same")
    nums4 = [2, 2, 2, 2]
    expected4 = 1
    result4 = solution.longestConsecutive(nums4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Negative numbers
    print("Test Case 5: Negative numbers")
    nums5 = [-1, -2, -3, -4]
    expected5 = 4
    result5 = solution.longestConsecutive(nums5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Mixed positive and negative numbers
    print("Test Case 6: Mixed positive and negative numbers")
    nums6 = [-1, 0, 1, 2, -2, 3, -3, 4, -4]
    expected6 = 9
    result6 = solution.longestConsecutive(nums6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Random order
    print("Test Case 7: Random order")
    nums7 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    expected7 = 10
    result7 = solution.longestConsecutive(nums7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Large input
    print("Test Case 8: Large input")
    nums8 = list(range(10000))
    expected8 = 10000
    result8 = solution.longestConsecutive(nums8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_longest_consecutive()
