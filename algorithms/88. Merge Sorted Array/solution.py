from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, n + m - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def test_merge():
    solution = Solution()

    # Test case 1: Basic case with elements in both arrays
    print("Test case 1: Basic case with elements in both arrays")
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected
    print("Passed")

    # Test case 2: nums1 empty, nums2 non-empty
    print("Test case 2: nums1 empty, nums2 non-empty")
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected = [1]
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected
    print("Passed")

    # Test case 3: nums2 empty, nums1 non-empty
    print("Test case 3: nums2 empty, nums1 non-empty")
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected = [1]
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected
    print("Passed")

    # Test case 4: Both arrays empty
    print("Test case 4: Both arrays empty")
    nums1 = []
    m = 0
    nums2 = []
    n = 0
    expected = []
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected
    print("Passed")

    # Test case 5: All elements in nums2 are smaller
    print("Test case 5: All elements in nums2 are smaller")
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    expected = [1, 2, 3, 4, 5, 6]
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected
    print("Passed")

    # Test case 6: All elements in nums2 are larger
    print("Test case 6: All elements in nums2 are larger")
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    expected = [1, 2, 3, 4, 5, 6]
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected
    print("Passed")

    # Test case 7: nums1 contains zeroes and positive numbers, nums2 contains negative numbers
    print(
        "Test case 7: nums1 contains zeroes and positive numbers, nums2 contains negative numbers"
    )
    nums1 = [0, 0, 3, 0, 0, 0]
    m = 3
    nums2 = [-3, -2, -1]
    n = 3
    expected = [-3, -2, -1, 0, 0, 3]
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected
    print("Passed")


if __name__ == "__main__":
    test_merge()
