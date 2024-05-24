from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = a + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result


def test_three_sum():
    solution = Solution()

    # Test case 1: Basic case with multiple triplets
    print("Test case 1: Basic case with multiple triplets")
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    result = solution.threeSum(nums)
    assert sorted(result) == sorted(expected)  # Sort results for comparison
    print("Passed")

    # Test case 2: No triplets
    print("Test case 2: No triplets")
    nums = [1, 2, -2, -1]
    expected = []
    result = solution.threeSum(nums)
    assert result == expected
    print("Passed")

    # Test case 3: All zeros
    print("Test case 3: All zeros")
    nums = [0, 0, 0, 0]
    expected = [[0, 0, 0]]
    result = solution.threeSum(nums)
    assert result == expected
    print("Passed")

    # Test case 4: Large input with multiple triplets
    print("Test case 4: Large input with multiple triplets")
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    expected = [
        [-4, 0, 4],
        [-4, 1, 3],
        [-3, -1, 4],
        [-3, 0, 3],
        [-3, 1, 2],
        [-2, -1, 3],
        [-2, 0, 2],
        [-1, -1, 2],
        [-1, 0, 1],
    ]
    result = solution.threeSum(nums)
    assert sorted(result) == sorted(expected)  # Sort results for comparison
    print("Passed")

    # Test case 5: Empty input
    print("Test case 5: Empty input")
    nums = []
    expected = []
    result = solution.threeSum(nums)
    assert result == expected
    print("Passed")

    # Test case 6: No triplet with zero sum
    print("Test case 6: No triplet with zero sum")
    nums = [1, -1, -1, 0]
    expected = [[-1, 0, 1]]
    result = solution.threeSum(nums)
    assert result == expected
    print("Passed")

    # Test case 7: Duplicates leading to same triplets
    print("Test case 7: Duplicates leading to same triplets")
    nums = [-2, 0, 1, 1, 2]
    expected = [[-2, 0, 2], [-2, 1, 1]]
    result = solution.threeSum(nums)
    assert sorted(result) == sorted(expected)  # Sort results for comparison
    print("Passed")

    # Test case 8: Triplets with positive and negative numbers
    print("Test case 8: Triplets with positive and negative numbers")
    nums = [-1, 2, -3, 4, -2, 1]
    expected = [[-3, -1, 4], [-3, 1, 2]]
    result = solution.threeSum(nums)
    assert sorted(result) == sorted(expected)  # Sort results for comparison
    print("Passed")


if __name__ == "__main__":
    test_three_sum()
