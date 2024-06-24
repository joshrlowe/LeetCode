from typing import List

"""
Bottom-Up (Tabulation) Solution
O(n) Time Complexity
O(1) Space Complexity
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        robNext, robNextNext = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            robNext, robNextNext = robNextNext, max(robNext + nums[i], robNextNext)

        return robNextNext


def test_rob():
    solution = Solution()

    # Test case 1: Regular case with multiple houses
    print("Test case 1: Regular case with multiple houses")
    nums = [1, 2, 3, 1]
    expected = 4
    result = solution.rob(nums)
    assert result == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Single house
    print("Test case 2: Single house")
    nums = [2]
    expected = 2
    result = solution.rob(nums)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Two houses
    print("Test case 3: Two houses")
    nums = [2, 3]
    expected = 3
    result = solution.rob(nums)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Larger number of houses
    print("Test case 4: Larger number of houses")
    nums = [2, 7, 9, 3, 1]
    expected = 12
    result = solution.rob(nums)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: All houses have the same value
    print("Test case 5: All houses have the same value")
    nums = [5, 5, 5, 5, 5]
    expected = 15
    result = solution.rob(nums)
    assert result == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Non-adjacent maximum value
    print("Test case 6: Non-adjacent maximum value")
    nums = [6, 7, 1, 30, 8, 2, 4]
    expected = 41
    result = solution.rob(nums)
    assert result == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_rob()
