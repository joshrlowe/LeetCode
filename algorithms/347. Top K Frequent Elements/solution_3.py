from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Start by creating a dictionary to store the frequencies of the numbers.
        In our past two solutions, the time complexity was dominated by how we
        obtain the top k frequencies from this dictionary. We can sort the list
        using TimSort, but this takes O(nlog(n)) time. We can use a heap to
        maintain the top k elements, but this takes O(n + nlog(k)) time in the end.

        How can we do better?

        Note that the maximum frequency that a number can have is len(nums), since
        there are len(nums) numbers in our list. Taking a leap of faith, we can
        perfom bucket sort on these frequencies, where indices of the array correspond
        to frequencies of numbers, and the numbers are values.

        From here, we can iterate through the frequencies array backwards to retrieve the
        top k elements. In summary, creating the dictionary takes O(n) time and O(n) space,
        populating the frequencies array takes O(n) time and O(n) space, and retrieving the
        top k elements takes O(n) time in the worst case. Therefore, this algorithm will
        take O(n) time in total, and we have reached an optimal solution.
        """
        count = defaultdict(lambda: 0)
        frequencies = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            frequencies[freq].append(num)

        res = []
        for i in range(len(frequencies) - 1, -1, -1):
            for num in frequencies[i]:
                res.append(num)
                if len(res) == k:
                    return res


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
