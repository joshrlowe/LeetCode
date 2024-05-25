from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


def test_get_concatenation():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [1, 2, 3]
    assert solution.getConcatenation(nums1) == [
        1,
        2,
        3,
        1,
        2,
        3,
    ], "Test Case 1 - Basic functionality test Failed"
    print("Passed")

    # Test Case 2: Empty list
    print("Test Case 2: Empty list")
    nums2 = []
    assert solution.getConcatenation(nums2) == [], "Test Case 2 - Empty list Failed"
    print("Passed")

    # Test Case 3: Single element
    print("Test Case 3: Single element")
    nums3 = [1]
    assert solution.getConcatenation(nums3) == [
        1,
        1,
    ], "Test Case 3 - Single element Failed"
    print("Passed")

    # Test Case 4: List with repeated elements
    print("Test Case 4: List with repeated elements")
    nums4 = [4, 4, 4]
    assert solution.getConcatenation(nums4) == [
        4,
        4,
        4,
        4,
        4,
        4,
    ], "Test Case 4 - List with repeated elements Failed"
    print("Passed")

    # Test Case 5: List with negative numbers
    print("Test Case 5: List with negative numbers")
    nums5 = [-1, -2, -3]
    assert solution.getConcatenation(nums5) == [
        -1,
        -2,
        -3,
        -1,
        -2,
        -3,
    ], "Test Case 5 - List with negative numbers Failed"
    print("Passed")

    # Test Case 6: List with mixed positive and negative numbers
    print("Test Case 6: List with mixed positive and negative numbers")
    nums6 = [-1, 0, 1]
    assert solution.getConcatenation(nums6) == [
        -1,
        0,
        1,
        -1,
        0,
        1,
    ], "Test Case 6 - List with mixed positive and negative numbers Failed"
    print("Passed")

    # Test Case 7: Large list
    print("Test Case 7: Large list")
    nums7 = list(range(1000))
    assert (
        solution.getConcatenation(nums7) == nums7 + nums7
    ), "Test Case 7 - Large list Failed"
    print("Passed")


if __name__ == "__main__":
    test_get_concatenation()
