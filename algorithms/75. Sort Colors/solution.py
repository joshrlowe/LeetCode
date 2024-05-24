from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        color_count = [0, 0, 0]
        for num in nums:
            match (num):
                case 0:
                    color_count[0] += 1
                case 1:
                    color_count[1] += 1
                case 2:
                    color_count[2] += 1
        i = 0
        for j in range(len(color_count)):
            for _ in range(color_count[j]):
                nums[i] = j
                i += 1


def test_sort_colors():
    solution = Solution()

    # Test case 1: Basic case with all colors
    print("Test case 1: Basic case with all colors")
    nums = [2, 0, 2, 1, 1, 0]
    expected = [0, 0, 1, 1, 2, 2]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 2: Already sorted
    print("Test case 2: Already sorted")
    nums = [0, 0, 1, 1, 2, 2]
    expected = [0, 0, 1, 1, 2, 2]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 3: Reverse sorted
    print("Test case 3: Reverse sorted")
    nums = [2, 2, 1, 1, 0, 0]
    expected = [0, 0, 1, 1, 2, 2]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 4: Single color (0)
    print("Test case 4: Single color (0)")
    nums = [0, 0, 0]
    expected = [0, 0, 0]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 5: Single color (1)
    print("Test case 5: Single color (1)")
    nums = [1, 1, 1]
    expected = [1, 1, 1]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 6: Single color (2)
    print("Test case 6: Single color (2)")
    nums = [2, 2, 2]
    expected = [2, 2, 2]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 7: Empty list
    print("Test case 7: Empty list")
    nums = []
    expected = []
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 8: Two colors (0 and 1)
    print("Test case 8: Two colors (0 and 1)")
    nums = [1, 0, 0, 1, 1, 0]
    expected = [0, 0, 0, 1, 1, 1]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 9: Two colors (1 and 2)
    print("Test case 9: Two colors (1 and 2)")
    nums = [2, 1, 1, 2, 1, 2]
    expected = [1, 1, 1, 2, 2, 2]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")

    # Test case 10: Two colors (0 and 2)
    print("Test case 10: Two colors (0 and 2)")
    nums = [2, 0, 2, 0, 2, 0]
    expected = [0, 0, 0, 2, 2, 2]
    solution.sortColors(nums)
    assert nums == expected
    print("Passed")


if __name__ == "__main__":
    test_sort_colors()
