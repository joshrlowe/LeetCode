from typing import List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        Time Complexity:
            Counting Frequencies: O(n), where n is the number of words;
            Building Heap: O(mlog(m)), where m is the number of unique words;
            Extracting Top K Elements: O(klog(m)), where k is the number of elements.
            In the worst case, every word is unique, and the time complexity would be O(nlog(n)).
        Space Complextiy:
            Dictionary: O(m)
            Heap: O(m)
            In the worst case, every word is unique, and the space complexity is O(n).
        '''
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        return [heapq.heappop(heap)[1] for _ in range(k)]