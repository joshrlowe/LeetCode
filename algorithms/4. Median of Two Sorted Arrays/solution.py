from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i + 1] if (i + 1) < len(A) else float("inf")
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j + 1] if (j + 1) < len(B) else float("inf")

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2:
                    return min(ARight, BRight)
                return (min(ARight, BRight) + max(ALeft, BLeft)) / 2
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1


def test_findMedianSortedArrays():
    solution = Solution()

    # Test case 1: Both arrays have the same length and no overlapping values
    print("Test case 1: Both arrays have the same length and no overlapping values")
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0
    assert (
        solution.findMedianSortedArrays(nums1, nums2) == expected
    ), f"Test case 1 failed"
    print("Passed")

    # Test case 2: Both arrays have different lengths and overlapping values
    print("Test case 2: Both arrays have different lengths and overlapping values")
    nums1 = [1, 2]
    nums2 = [3, 4]
    expected = 2.5
    assert (
        solution.findMedianSortedArrays(nums1, nums2) == expected
    ), f"Test case 2 failed"
    print("Passed")

    # Test case 3: One array is empty
    print("Test case 3: One array is empty")
    nums1 = []
    nums2 = [1]
    expected = 1.0
    assert (
        solution.findMedianSortedArrays(nums1, nums2) == expected
    ), f"Test case 3 failed"
    print("Passed")

    # Test case 4: Both arrays have one element each
    print("Test case 4: Both arrays have one element each")
    nums1 = [1]
    nums2 = [2]
    expected = 1.5
    assert (
        solution.findMedianSortedArrays(nums1, nums2) == expected
    ), f"Test case 4 failed"
    print("Passed")

    # Test case 5: Both arrays have multiple elements
    print("Test case 5: Both arrays have multiple elements")
    nums1 = [1, 3, 8]
    nums2 = [7, 9, 10, 11]
    expected = 8.0
    assert (
        solution.findMedianSortedArrays(nums1, nums2) == expected
    ), f"Test case 5 failed"
    print("Passed")

    # Test case 6: Both arrays have the same elements
    print("Test case 6: Both arrays have the same elements")
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    expected = 2.0
    assert (
        solution.findMedianSortedArrays(nums1, nums2) == expected
    ), f"Test case 6 failed"
    print("Passed")

    # Test case 7: Arrays with negative numbers
    print("Test case 7: Arrays with negative numbers")
    nums1 = [-5, 3, 6, 12, 15]
    nums2 = [-12, -10, -6, -3, 4, 10]
    expected = 3.0
    assert (
        solution.findMedianSortedArrays(nums1, nums2) == expected
    ), f"Test case 7 failed"
    print("Passed")

    # Test case 8: Arrays with repeated elements
    print("Test case 8: Arrays with repeated elements")
    nums1 = [1, 2, 2]
    nums2 = [2, 3, 4]
    expected = 2.0
    assert (
        solution.findMedianSortedArrays(nums1, nums2) == expected
    ), f"Test case 8 failed"
    print("Passed")


if __name__ == "__main__":
    test_findMedianSortedArrays()
