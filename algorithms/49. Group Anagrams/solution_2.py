from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return result.values()


def test_group_anagrams():
    solution = Solution()

    # Test case 1: Basic case with mixed anagrams
    print("Test case 1: Basic case with mixed anagrams")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected]
    )
    print("Passed")

    # Test case 2: Single anagram group
    print("Test case 2: Single anagram group")
    strs = [""]
    expected = [[""]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected]
    )
    print("Passed")

    # Test case 3: No anagrams
    print("Test case 3: No anagrams")
    strs = ["a", "b", "c"]
    expected = [["a"], ["b"], ["c"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected]
    )
    print("Passed")

    # Test case 4: Anagrams with different lengths
    print("Test case 4: Anagrams with different lengths")
    strs = ["abc", "bca", "cab", "a", "b", "c"]
    expected = [["abc", "bca", "cab"], ["a"], ["b"], ["c"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected]
    )
    print("Passed")

    # Test case 5: Large input with multiple anagram groups
    print("Test case 5: Large input with multiple anagram groups")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "ant", "tna"]
    expected = [["eat", "tea", "ate"], ["tan", "nat", "ant", "tna"], ["bat", "tab"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected]
    )
    print("Passed")

    # Test case 6: Single character anagrams
    print("Test case 6: Single character anagrams")
    strs = ["a", "a", "a"]
    expected = [["a", "a", "a"]]
    result = solution.groupAnagrams(strs)
    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected]
    )
    print("Passed")


if __name__ == "__main__":
    test_group_anagrams()
