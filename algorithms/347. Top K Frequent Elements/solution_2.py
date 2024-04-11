from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Create a dictionary that stores the frequencies of numbers.
        Create a heap of size k, where we iterate through n elements
        to construct a min heap, and if the next element is smaller than
        the minimum element, pop from the min heap and insert the new element in.
        So, in the end, we will have a min heap containing the 7 largest elements.
        Time Complexity: O(n + nlog(k))
        """
        frequencies = defaultdict(lambda: 0)
        for num in nums:
            frequencies[num] += 1
        return heapq.nlargest(k, frequencies, key=frequencies.get)
