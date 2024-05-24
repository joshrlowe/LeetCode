from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[i], nums[k] = nums[k], nums[i]
        return k + 1 if len(nums) != 0 else 0


def test_remove_duplicates():
    solution = Solution()

    # Test case 1: Basic case with duplicates
    print("Test case 1: Basic case with duplicates")
    nums = [1, 1, 2]
    expected_length = 2
    expected_nums = [1, 2]
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

    # Test case 3: All duplicates
    print("Test case 3: All duplicates")
    nums = [2, 2, 2, 2, 2]
    expected_length = 1
    expected_nums = [2]
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

    # Test case 6: Large list with multiple duplicates
    print("Test case 6: Large list with multiple duplicates")
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_length = 5
    expected_nums = [0, 1, 2, 3, 4]
    result_length = solution.removeDuplicates(nums)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")


if __name__ == "__main__":
    test_remove_duplicates()
