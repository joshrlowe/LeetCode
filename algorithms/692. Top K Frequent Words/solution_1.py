from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Time Complexity:
            Counting Frequencies in count: O(n), where n is the number of words in words;
            Placing numbers in frequencies: O(m), where m is the number of unique words;
            Sorting each frequency: In the worst case, O(nlog(n)) if every word has the same frequency, but we only do this once.
            In the worst case, each word is unique and occurs once, and the time complexity is O(nlog(n)).
        Space Complexity:
            count: O(m)
            frequencies: O(n)
            The total space complexity is O(n).
        """
        res = []
        count = {}
        frequencies = [[] for _ in range(len(words) + 1)]
        for word in words:
            count[word] = count.get(word, 0) + 1
        for word, freq in count.items():
            frequencies[freq].append(word)
        for i in range(len(frequencies) - 1, -1, -1):
            for word in sorted(frequencies[i]):
                res.append(word)
                if len(res) == k:
                    return res
