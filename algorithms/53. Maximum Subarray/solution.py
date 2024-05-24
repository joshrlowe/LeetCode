from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        prefix = nums[0]
        for i in range(1, len(nums)):
            if prefix < 0:
                prefix = nums[i]
            else:
                prefix += nums[i]
            if prefix > global_sum:
                global_sum = prefix
        return global_sum


def test_max_sub_array():
    solution = Solution()

    # Test case 1: Basic case with positive and negative numbers
    print("Test case 1: Basic case with positive and negative numbers")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6  # [4,-1,2,1] has the largest sum = 6
    result = solution.maxSubArray(nums)
    assert result == expected
    print("Passed")

    # Test case 2: All positive numbers
    print("Test case 2: All positive numbers")
    nums = [1, 2, 3, 4, 5]
    expected = 15  # The entire array has the largest sum = 15
    result = solution.maxSubArray(nums)
    assert result == expected
    print("Passed")

    # Test case 3: All negative numbers
    print("Test case 3: All negative numbers")
    nums = [-1, -2, -3, -4]
    expected = -1  # The largest single element is -1
    result = solution.maxSubArray(nums)
    assert result == expected
    print("Passed")

    # Test case 4: Single element
    print("Test case 4: Single element")
    nums = [5]
    expected = 5  # Only one element, so the largest sum is 5
    result = solution.maxSubArray(nums)
    assert result == expected
    print("Passed")

    # Test case 5: Mixed numbers with the largest sum at the end
    print("Test case 5: Mixed numbers with the largest sum at the end")
    nums = [1, 2, 3, -2, 5]
    expected = 9  # [1, 2, 3, -2, 5] has the largest sum = 9
    result = solution.maxSubArray(nums)
    assert result == expected
    print("Passed")

    # Test case 6: Large numbers
    print("Test case 6: Large numbers")
    nums = [1000000, -1, 1000000, -1, 1000000]
    expected = (
        2999998  # [1000000, -1, 1000000, -1, 1000000] has the largest sum = 2999998
    )
    result = solution.maxSubArray(nums)
    assert result == expected
    print("Passed")

    # Test case 7: Alternating positive and negative numbers
    print("Test case 7: Alternating positive and negative numbers")
    nums = [2, -1, 2, -1, 2]
    expected = 4  # [2, -1, 2, -1, 2] has the largest sum = 4
    result = solution.maxSubArray(nums)
    assert result == expected
    print("Passed")


if __name__ == "__main__":
    test_max_sub_array()
