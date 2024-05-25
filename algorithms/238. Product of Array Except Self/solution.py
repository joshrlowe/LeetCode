from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Each number is equal to the product of all terms to the left times the product of all terms to the right
        So, if we multiply from the left then multiply from the right, then we would get the product of array
        except self in O(2n) \in O(n) time.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = [1] * len(nums)
        left, right = 1, 1
        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


def test_product_except_self():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    result1 = solution.productExceptSelf(nums1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Contains zero
    print("Test Case 2: Contains zero")
    nums2 = [1, 2, 0, 4]
    expected2 = [0, 0, 8, 0]
    result2 = solution.productExceptSelf(nums2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Contains zero Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: All zeros
    print("Test Case 3: All zeros")
    nums3 = [0, 0, 0, 0]
    expected3 = [0, 0, 0, 0]
    result3 = solution.productExceptSelf(nums3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - All zeros Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single element
    print("Test Case 4: Single element")
    nums4 = [10]
    expected4 = [1]
    result4 = solution.productExceptSelf(nums4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Single element Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Two elements
    print("Test Case 5: Two elements")
    nums5 = [3, 5]
    expected5 = [5, 3]
    result5 = solution.productExceptSelf(nums5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Two elements Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Negative numbers
    print("Test Case 6: Negative numbers")
    nums6 = [-1, -2, -3, -4]
    expected6 = [-24, -12, -8, -6]
    result6 = solution.productExceptSelf(nums6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Negative numbers Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Mixed positive and negative numbers
    print("Test Case 7: Mixed positive and negative numbers")
    nums7 = [-1, 2, -3, 4]
    expected7 = [-24, 12, -8, 6]
    result7 = solution.productExceptSelf(nums7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Mixed positive and negative numbers Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: All ones
    print("Test Case 8: All ones")
    nums8 = [1, 1, 1, 1]
    expected8 = [1, 1, 1, 1]
    result8 = solution.productExceptSelf(nums8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - All ones Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_product_except_self()
