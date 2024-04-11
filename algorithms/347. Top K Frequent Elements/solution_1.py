from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach 2
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
