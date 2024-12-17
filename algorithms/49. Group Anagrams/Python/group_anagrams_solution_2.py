from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        result[tuple(count)].append(s)
    return result.values()
