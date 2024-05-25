from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sum = 0
        for num in nums:
            sum += num
            self.prefix.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        preLeft = self.prefix[left - 1] if left > 0 else 0
        preRight = self.prefix[right]
        return preRight - preLeft


def test_num_array():
    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [-2, 0, 3, -5, 2, -1]
    num_array1 = NumArray(nums1)
    assert (
        num_array1.sumRange(0, 2) == 1
    ), f"Test Case 1 - sumRange(0, 2) Failed: Expected 1, got {num_array1.sumRange(0, 2)}"
    assert (
        num_array1.sumRange(2, 5) == -1
    ), f"Test Case 1 - sumRange(2, 5) Failed: Expected -1, got {num_array1.sumRange(2, 5)}"
    assert (
        num_array1.sumRange(0, 5) == -3
    ), f"Test Case 1 - sumRange(0, 5) Failed: Expected -3, got {num_array1.sumRange(0, 5)}"
    print("Passed")

    # Test Case 2: Single element
    print("Test Case 2: Single element")
    nums2 = [1]
    num_array2 = NumArray(nums2)
    assert (
        num_array2.sumRange(0, 0) == 1
    ), f"Test Case 2 - sumRange(0, 0) Failed: Expected 1, got {num_array2.sumRange(0, 0)}"
    print("Passed")

    # Test Case 3: All elements are zero
    print("Test Case 3: All elements are zero")
    nums3 = [0, 0, 0, 0]
    num_array3 = NumArray(nums3)
    assert (
        num_array3.sumRange(0, 3) == 0
    ), f"Test Case 3 - sumRange(0, 3) Failed: Expected 0, got {num_array3.sumRange(0, 3)}"
    assert (
        num_array3.sumRange(1, 2) == 0
    ), f"Test Case 3 - sumRange(1, 2) Failed: Expected 0, got {num_array3.sumRange(1, 2)}"
    print("Passed")

    # Test Case 4: Range at the end of the array
    print("Test Case 4: Range at the end of the array")
    nums4 = [1, 2, 3, 4, 5]
    num_array4 = NumArray(nums4)
    assert (
        num_array4.sumRange(3, 4) == 9
    ), f"Test Case 4 - sumRange(3, 4) Failed: Expected 9, got {num_array4.sumRange(3, 4)}"
    assert (
        num_array4.sumRange(1, 3) == 9
    ), f"Test Case 4 - sumRange(1, 3) Failed: Expected 9, got {num_array4.sumRange(1, 3)}"
    print("Passed")

    # Test Case 5: Negative numbers
    print("Test Case 5: Negative numbers")
    nums5 = [-1, -2, -3, -4, -5]
    num_array5 = NumArray(nums5)
    assert (
        num_array5.sumRange(0, 2) == -6
    ), f"Test Case 5 - sumRange(0, 2) Failed: Expected -6, got {num_array5.sumRange(0, 2)}"
    assert (
        num_array5.sumRange(1, 4) == -14
    ), f"Test Case 5 - sumRange(1, 4) Failed: Expected -14, got {num_array5.sumRange(1, 4)}"
    print("Passed")

    # Test Case 6: Mix of positive and negative numbers
    print("Test Case 6: Mix of positive and negative numbers")
    nums6 = [1, -1, 2, -2, 3, -3]
    num_array6 = NumArray(nums6)
    assert (
        num_array6.sumRange(0, 5) == 0
    ), f"Test Case 6 - sumRange(0, 5) Failed: Expected 0, got {num_array6.sumRange(0, 5)}"
    assert (
        num_array6.sumRange(2, 4) == 3
    ), f"Test Case 6 - sumRange(2, 4) Failed: Expected 3, got {num_array6.sumRange(2, 4)}"
    print("Passed")


if __name__ == "__main__":
    test_num_array()
