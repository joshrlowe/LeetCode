from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = 0

        for num in nums:
            if count == 0:
                element = num
            elif element == num:
                count += 1
            else:
                count -= 1
        return element


def test_majority_element():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [3, 2, 3]
    expected1 = 3
    result1 = solution.majorityElement(nums1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single element
    print("Test Case 2: Single element")
    nums2 = [1]
    expected2 = 1
    result2 = solution.majorityElement(nums2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Single element Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: All elements the same
    print("Test Case 3: All elements the same")
    nums3 = [2, 2, 2, 2]
    expected3 = 2
    result3 = solution.majorityElement(nums3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - All elements the same Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Large array with clear majority
    print("Test Case 4: Large array with clear majority")
    nums4 = [1, 1, 1, 2, 2, 2, 2, 2]
    expected4 = 2
    result4 = solution.majorityElement(nums4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Large array with clear majority Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Majority element at the end
    print("Test Case 5: Majority element at the end")
    nums5 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    expected5 = 4
    result5 = solution.majorityElement(nums5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Majority element at the end Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Majority element in the middle
    print("Test Case 6: Majority element in the middle")
    nums6 = [2, 2, 1, 1, 2, 2, 2]
    expected6 = 2
    result6 = solution.majorityElement(nums6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Majority element in the middle Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Large input
    print("Test Case 7: Large input")
    nums7 = [1] * 50000 + [2] * 50001
    expected7 = 2
    result7 = solution.majorityElement(nums7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Large input Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_majority_element()
