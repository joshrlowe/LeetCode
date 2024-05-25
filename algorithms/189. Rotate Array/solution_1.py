from typing import List


#
class Solution:
    # Self-created approach - good if I wanted to show I know how reverse could be implemented for indices
    # O(n) time complexity
    # O(1) space complexity
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_indices(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        nums.reverse()
        reverse_indices(0, k - 1)
        reverse_indices(k, len(nums) - 1)


def test_rotate():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    expected1 = [5, 6, 7, 1, 2, 3, 4]
    solution.rotate(nums1, k1)
    assert nums1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {nums1}"
    print("Passed")

    # Test Case 2: Rotate by zero
    print("Test Case 2: Rotate by zero")
    nums2 = [1, 2, 3, 4, 5]
    k2 = 0
    expected2 = [1, 2, 3, 4, 5]
    solution.rotate(nums2, k2)
    assert nums2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {nums2}"
    print("Passed")

    # Test Case 3: Rotate by the length of the array
    print("Test Case 3: Rotate by the length of the array")
    nums3 = [1, 2, 3, 4, 5]
    k3 = 5
    expected3 = [1, 2, 3, 4, 5]
    solution.rotate(nums3, k3)
    assert nums3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {nums3}"
    print("Passed")

    # Test Case 4: Rotate by more than the length of the array
    print("Test Case 4: Rotate by more than the length of the array")
    nums4 = [1, 2, 3, 4, 5]
    k4 = 7  # Equivalent to rotating by 2
    expected4 = [4, 5, 1, 2, 3]
    solution.rotate(nums4, k4)
    assert nums4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {nums4}"
    print("Passed")

    # Test Case 5: Single element array
    print("Test Case 5: Single element array")
    nums5 = [1]
    k5 = 3
    expected5 = [1]
    solution.rotate(nums5, k5)
    assert nums5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {nums5}"
    print("Passed")

    # Test Case 6: All elements the same
    print("Test Case 6: All elements the same")
    nums6 = [1, 1, 1, 1, 1]
    k6 = 3
    expected6 = [1, 1, 1, 1, 1]
    solution.rotate(nums6, k6)
    assert nums6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {nums6}"
    print("Passed")

    # Test Case 7: Large rotation
    print("Test Case 7: Large rotation")
    nums7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k7 = 1003  # Equivalent to rotating by 3
    expected7 = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums7, k7)
    assert nums7 == expected7, f"Test Case 7 Failed: Expected {expected7}, got {nums7}"
    print("Passed")


if __name__ == "__main__":
    test_rotate()
