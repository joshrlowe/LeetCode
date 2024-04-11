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
