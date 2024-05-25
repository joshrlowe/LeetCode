from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Iterate through the list and count the frequencies in a hash map - O(n)
        Convert the dictionary items to a list (will be a list of tuples) - O(n)
        Sort the list of tuples, with a key being the second item in each tuple, i.e., the frequency - O(nlog(n))
        Return the number at index 0 for the last k elements in the sorted list of tuples - O(k)

        Time Complexity: O(n + n + nlog(n) + k) = O(nlog(n))
        Space Complexity: O(n + k) = O(n + k)
        """
        frequencies = defaultdict(lambda: 0)
        for num in nums:
            frequencies[num] += 1
        return [
            x[0] for x in sorted(list(frequencies.items()), key=lambda x: x[1])[-k:]
        ]


def test_top_k_frequent():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    expected1 = [1, 2]
    result1 = solution.topKFrequent(nums1, k1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Single element with highest frequency
    print("Test Case 2: Single element with highest frequency")
    nums2 = [1]
    k2 = 1
    expected2 = [1]
    result2 = solution.topKFrequent(nums2, k2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Single element with highest frequency Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Negative numbers with frequency
    print("Test Case 3: Negative numbers with frequency")
    nums4 = [-1, -1, -2, -2, -3]
    k4 = 2
    expected4 = [-1, -2]
    result4 = solution.topKFrequent(nums4, k4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Negative numbers with frequency Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 4: All elements are the same
    print("Test Case 4: All elements are the same")
    nums5 = [1, 1, 1, 1]
    k5 = 1
    expected5 = [1]
    result5 = solution.topKFrequent(nums5, k5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - All elements are the same Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 5: k equal to the length of the list
    print("Test Case 5: k equal to the length of the list")
    nums6 = [1, 2, 2, 3, 3, 3]
    k6 = 3
    expected6 = [3, 2, 1]
    result6 = solution.topKFrequent(nums6, k6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - k equal to the length of the list Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 6: Larger k value
    print("Test Case 6: Larger k value")
    nums7 = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4]
    k7 = 4
    expected7 = [4, 1, 2, 3]
    result7 = solution.topKFrequent(nums7, k7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Larger k value Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_top_k_frequent()
