from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]


def test_two_sum():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [1, 2]
    result1 = solution.twoSum(numbers1, target1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Larger numbers
    print("Test Case 2: Larger numbers")
    numbers2 = [10, 20, 30, 40, 50]
    target2 = 90
    expected2 = [4, 5]
    result2 = solution.twoSum(numbers2, target2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Negative numbers
    print("Test Case 3: Negative numbers")
    numbers3 = [-3, -2, 0, 3, 5]
    target3 = 0
    expected3 = [1, 4]
    result3 = solution.twoSum(numbers3, target3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Two large numbers
    print("Test Case 4: Two large numbers")
    numbers7 = [1, 2, 3, 999999999, 1000000000]
    target7 = 1999999999
    expected7 = [4, 5]
    result7 = solution.twoSum(numbers7, target7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_two_sum()
