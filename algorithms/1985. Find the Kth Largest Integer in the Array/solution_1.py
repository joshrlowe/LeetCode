# Self-Implemented Sorting
# O(nlog(n)) time complexity
# O(n) space complexity
def kthLargestNumber(nums, k) -> str:
    def merge_sort(lst):
        if len(lst) < 2:
            return lst
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        i, j = 0, 0
        new_lst = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                new_lst.append(left[i])
                i += 1
            else:
                new_lst.append(right[j])
                j += 1
        new_lst.extend(left[i:])
        new_lst.extend(right[j:])
        lst = new_lst
        return lst

    nums = [int(num) for num in nums]
    nums = merge_sort(nums)
    return str(nums[-k])


def test_kth_largest_number():
    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = ["3", "6", "7", "10"]
    k1 = 4
    assert (
        kthLargestNumber(nums1, k1) == "3"
    ), "Test Case 1 - Basic functionality test Failed"
    print("Passed")

    # Test Case 2: Small array
    print("Test Case 2: Small array")
    nums2 = ["2", "1"]
    k2 = 1
    assert kthLargestNumber(nums2, k2) == "2", "Test Case 2 - Small array Failed"
    print("Passed")

    # Test Case 3: Single element
    print("Test Case 3: Single element")
    nums3 = ["5"]
    k3 = 1
    assert kthLargestNumber(nums3, k3) == "5", "Test Case 3 - Single element Failed"
    print("Passed")

    # Test Case 4: Larger array with duplicates
    print("Test Case 4: Larger array with duplicates")
    nums4 = ["3", "3", "3", "3", "3"]
    k4 = 3
    assert (
        kthLargestNumber(nums4, k4) == "3"
    ), "Test Case 4 - Larger array with duplicates Failed"
    print("Passed")

    # Test Case 5: k is in the middle of the array
    print("Test Case 5: k is in the middle of the array")
    nums5 = ["3", "5", "2", "4", "6", "8"]
    k5 = 3
    assert (
        kthLargestNumber(nums5, k5) == "5"
    ), "Test Case 5 - k is in the middle of the array Failed"
    print("Passed")

    # Test Case 6: Array with negative numbers
    print("Test Case 6: Array with negative numbers")
    nums6 = ["-3", "-1", "-2", "-4", "-5"]
    k6 = 2
    assert (
        kthLargestNumber(nums6, k6) == "-2"
    ), "Test Case 6 - Array with negative numbers Failed"
    print("Passed")

    # Test Case 7: Mixed positive and negative numbers
    print("Test Case 7: Mixed positive and negative numbers")
    nums7 = ["-3", "1", "-2", "4", "-5"]
    k7 = 4
    assert (
        kthLargestNumber(nums7, k7) == "-3"
    ), "Test Case 7 - Mixed positive and negative numbers Failed"
    print("Passed")

    # Test Case 8: Large values
    print("Test Case 8: Large values")
    nums8 = ["1000000000", "999999999", "1000000001"]
    k8 = 2
    assert (
        kthLargestNumber(nums8, k8) == "1000000000"
    ), "Test Case 8 - Large values Failed"
    print("Passed")


if __name__ == "__main__":
    test_kth_largest_number()
