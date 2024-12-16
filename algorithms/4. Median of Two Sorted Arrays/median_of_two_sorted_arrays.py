from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
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
