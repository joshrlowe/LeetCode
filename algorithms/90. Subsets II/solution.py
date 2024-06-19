from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i >= len(nums):
                subsets.append(current[:])
                return

            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        subsets, current = [], []
        nums.sort()
        backtrack(0)
        return subsets


def test_subsetsWithDup():
    solution = Solution()

    # Test case 1: Regular case with duplicates
    print("Test case 1: Regular case with duplicates")
    nums = [1, 2, 2]
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    result = solution.subsetsWithDup(nums)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: Regular case with no duplicates
    print("Test case 2: Regular case with no duplicates")
    nums = [1, 2, 3]
    expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    result = solution.subsetsWithDup(nums)
    assert sorted(result) == sorted(expected), "Test case 2 failed"
    print("Passed")

    # Test case 3: Single element
    print("Test case 3: Single element")
    nums = [1]
    expected = [[], [1]]
    result = solution.subsetsWithDup(nums)
    assert sorted(result) == sorted(expected), "Test case 3 failed"
    print("Passed")

    # Test case 4: Empty list
    print("Test case 4: Empty list")
    nums = []
    expected = [[]]
    result = solution.subsetsWithDup(nums)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: All elements are the same
    print("Test case 5: All elements are the same")
    nums = [2, 2, 2]
    expected = [[], [2], [2, 2], [2, 2, 2]]
    result = solution.subsetsWithDup(nums)
    assert sorted(result) == sorted(expected), "Test case 5 failed"
    print("Passed")

    # Test case 6: Mixed positive and negative numbers
    print("Test case 6: Mixed positive and negative numbers")
    nums = [-1, 0, 1]
    expected = [[], [-1], [-1, 0], [-1, 0, 1], [-1, 1], [0], [0, 1], [1]]
    result = solution.subsetsWithDup(nums)
    assert sorted(result) == sorted(expected), "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_subsetsWithDup()
