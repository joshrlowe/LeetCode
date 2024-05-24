from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return k


def test_remove_element():
    solution = Solution()

    # Test case 1: Basic case with elements to remove
    print("Test case 1: Basic case with elements to remove")
    nums = [3, 2, 2, 3]
    val = 3
    expected_length = 2
    expected_nums = [2, 2]
    result_length = solution.removeElement(nums, val)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 2: No elements to remove
    print("Test case 2: No elements to remove")
    nums = [1, 2, 3, 4]
    val = 5
    expected_length = 4
    expected_nums = [1, 2, 3, 4]
    result_length = solution.removeElement(nums, val)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 3: All elements to remove
    print("Test case 3: All elements to remove")
    nums = [4, 4, 4, 4]
    val = 4
    expected_length = 0
    expected_nums = []
    result_length = solution.removeElement(nums, val)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 4: Empty list
    print("Test case 4: Empty list")
    nums = []
    val = 1
    expected_length = 0
    expected_nums = []
    result_length = solution.removeElement(nums, val)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 5: Single element to remove
    print("Test case 5: Single element to remove")
    nums = [1]
    val = 1
    expected_length = 0
    expected_nums = []
    result_length = solution.removeElement(nums, val)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 6: Single element not to remove
    print("Test case 6: Single element not to remove")
    nums = [1]
    val = 2
    expected_length = 1
    expected_nums = [1]
    result_length = solution.removeElement(nums, val)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")

    # Test case 7: Mixed elements with and without value to remove
    print("Test case 7: Mixed elements with and without value to remove")
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected_length = 5
    expected_nums = [0, 1, 3, 0, 4]
    result_length = solution.removeElement(nums, val)
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    print("Passed")


if __name__ == "__main__":
    test_remove_element()
