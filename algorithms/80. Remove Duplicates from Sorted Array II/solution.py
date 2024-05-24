from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if k - 2 < 0 or nums[i] != nums[k - 2]:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return k


def test_remove_duplicates():
    solution = Solution()

    # Test case 1: Basic case with duplicates
    print("Test case 1: Basic case with duplicates")
    nums = [1, 1, 1, 2, 2, 3]
    expected_length = 5
    expected_nums = [1, 1, 2, 2, 3]
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 2: No duplicates
    print("Test case 2: No duplicates")
    nums = [1, 2, 3, 4]
    expected_length = 4
    expected_nums = [1, 2, 3, 4]
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 3: All elements are duplicates
    print("Test case 3: All elements are duplicates")
    nums = [1, 1, 1, 1, 1]
    expected_length = 2
    expected_nums = [1, 1]
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 4: Empty list
    print("Test case 4: Empty list")
    nums = []
    expected_length = 0
    expected_nums = []
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 5: Single element list
    print("Test case 5: Single element list")
    nums = [1]
    expected_length = 1
    expected_nums = [1]
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 6: Two element list with duplicates
    print("Test case 6: Two element list with duplicates")
    nums = [1, 1]
    expected_length = 2
    expected_nums = [1, 1]
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 7: Larger list with more complex duplicates
    print("Test case 7: Larger list with more complex duplicates")
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected_length = 7
    expected_nums = [0, 0, 1, 1, 2, 3, 3]
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 8: Multiple elements with no removal needed
    print("Test case 8: Multiple elements with no removal needed")
    nums = [1, 1, 2, 2, 3, 3]
    expected_length = 6
    expected_nums = [1, 1, 2, 2, 3, 3]
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")


if __name__ == "__main__":
    test_remove_duplicates()
