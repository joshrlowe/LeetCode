from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i


def test_two_sum():
    solution = Solution()

    # Test case 1: Basic case
    print("Test case 1: Basic case")
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1]  # 2 + 7 = 9
    print("Passed")

    # Test case 2: Multiple pairs, return first correct pair
    print("Test case 2: Multiple pairs, return first correct pair")
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]  # 2 + 4 = 6
    print("Passed")

    # Test case 3: Negative numbers
    print("Test case 3: Negative numbers")
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert solution.twoSum(nums, target) == [2, 4]  # -3 + -5 = -8
    print("Passed")

    # Test case 4: Zero in the list
    print("Test case 4: Zero in the list")
    nums = [0, 4, 3, 0]
    target = 0
    assert solution.twoSum(nums, target) == [0, 3]  # 0 + 0 = 0
    print("Passed")

    # Test case 5: Large numbers
    print("Test case 5: Large numbers")
    nums = [1_000_000, 2_000_000, 3_000_000, 1_000_000]
    target = 2_000_000
    assert solution.twoSum(nums, target) == [0, 3]  # 1_000_000 + 1_000_000 = 2_000_000
    print("Passed")

    # Test case 6: Single pair, edge case
    print("Test case 6: Single pair, edge case")
    nums = [1, 3]
    target = 4
    assert solution.twoSum(nums, target) == [0, 1]  # 1 + 3 = 4
    print("Passed")

    # Test case 7: No solution (should not happen as per problem statement, but good to test)
    print("Test case 7: No solution")
    nums = [1, 2, 3]
    target = 7
    assert solution.twoSum(nums, target) is None  # No pair sums to 7
    print("Passed")


if __name__ == "__main__":
    test_two_sum()
