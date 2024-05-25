from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallerSums = 0
        for i, a in enumerate(nums):
            new_target = target - a
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < new_target:
                    smallerSums += r - l
                    l += 1
                else:
                    r -= 1
        return smallerSums


def test_three_sum_smaller():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [-2, 0, 1, 3]
    target1 = 2
    expected1 = 2
    result1 = solution.threeSumSmaller(nums1, target1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: All elements the same
    print("Test Case 2: All elements the same")
    nums2 = [1, 1, 1, 1]
    target2 = 5
    expected2 = 4
    result2 = solution.threeSumSmaller(nums2, target2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - All elements the same Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: No triplet less than target
    print("Test Case 3: No triplet less than target")
    nums3 = [1, 2, 3, 4]
    target3 = 3
    expected3 = 0
    result3 = solution.threeSumSmaller(nums3, target3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - No triplet less than target Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Large numbers
    print("Test Case 4: Large numbers")
    nums4 = [10, 20, 30, 40, 50]
    target4 = 100
    expected4 = 6
    result4 = solution.threeSumSmaller(nums4, target4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Large numbers Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Negative numbers
    print("Test Case 5: Negative numbers")
    nums5 = [-2, -1, 0, 1]
    target5 = 2
    expected5 = 4
    result5 = solution.threeSumSmaller(nums5, target5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Negative numbers Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Mixed positive and negative numbers
    print("Test Case 6: Mixed positive and negative numbers")
    nums6 = [-1, 0, 1, 2, -1, -4]
    target6 = 2
    expected6 = 17
    result6 = solution.threeSumSmaller(nums6, target6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Mixed positive and negative numbers Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Single triplet
    print("Test Case 7: Single triplet")
    nums7 = [1, 2, 3]
    target7 = 7
    expected7 = 1
    result7 = solution.threeSumSmaller(nums7, target7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Single triplet Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Larger target
    print("Test Case 8: Larger target")
    nums8 = [1, 2, 3, 4, 5]
    target8 = 10
    expected8 = 6
    result8 = solution.threeSumSmaller(nums8, target8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Larger target Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: All negative numbers
    print("Test Case 9: All negative numbers")
    nums9 = [-4, -3, -2, -1]
    target9 = -2
    expected9 = 4
    result9 = solution.threeSumSmaller(nums9, target9)
    assert (
        result9 == expected9
    ), f"Test Case 9 - All negative numbers Failed: Expected {expected9}, got {result9}"
    print("Passed")


if __name__ == "__main__":
    test_three_sum_smaller()
