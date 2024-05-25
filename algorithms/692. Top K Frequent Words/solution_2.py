from typing import List
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Time Complexity:
            Counting Frequencies: O(n), where n is the number of words;
            Building Heap: O(mlog(m)), where m is the number of unique words;
            Extracting Top K Elements: O(klog(m)), where k is the number of elements.
            In the worst case, every word is unique, and the time complexity would be O(nlog(n)).
        Space Complextiy:
            Dictionary: O(m)
            Heap: O(m)
            In the worst case, every word is unique, and the space complexity is O(n).
        """
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        return [heapq.heappop(heap)[1] for _ in range(k)]


def test_top_k_frequent():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    words1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k1 = 2
    expected1 = ["i", "love"]
    result1 = solution.topKFrequent(words1, k1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Tie in frequencies
    print("Test Case 2: Tie in frequencies")
    words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k2 = 4
    expected2 = ["the", "is", "sunny", "day"]
    result2 = solution.topKFrequent(words2, k2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Tie in frequencies Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single word repeated
    print("Test Case 3: Single word repeated")
    words3 = ["word", "word", "word"]
    k3 = 1
    expected3 = ["word"]
    result3 = solution.topKFrequent(words3, k3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Single word repeated Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: All words with the same frequency
    print("Test Case 4: All words with the same frequency")
    words4 = ["a", "b", "c", "d"]
    k4 = 2
    expected4 = ["a", "b"]  # or any combination of two words, alphabetically sorted
    result4 = solution.topKFrequent(words4, k4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - All words with the same frequency Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Words with the same frequency but different lexicographical order
    print(
        "Test Case 5: Words with the same frequency but different lexicographical order"
    )
    words7 = ["aa", "bb", "cc", "aa", "bb", "cc", "dd"]
    k7 = 3
    expected7 = ["aa", "bb", "cc"]
    result7 = solution.topKFrequent(words7, k7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Words with the same frequency but different lexicographical order Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_top_k_frequent()
